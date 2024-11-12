import openai
import os
from pywebio import start_server
from pywebio.output import put_markdown, put_file, put_text
from pywebio.input import input, radio, NUMBER
from io import BytesIO
import pandas as pd
import json

# Ensure API key is set
openai.api_key = os.getenv("OPEsk-proj-EEphWp6cHL1Lae6nqafI69Ne-i7vkBpuw5ZI4MQATBk4QLn7ndp_XE0p8wtE9I7ayYdr0ahTnET3BlbkFJ4x2QMjZf0-9u2kiwrjaPIvhKAXo9TaNEczQ_ttCgFa5ptiufyefEv94t-8w5t4ZvsTnoV3sikA")
if not openai.api_key:
    raise EnvironmentError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

# Function to generate data with error handling
def generate_data_with_chatgpt(num_entries, include_political):
    try:
        # Construct prompt for ChatGPT
        prompt = (
            f"Generate {num_entries} entries of fictional data with the following fields: "
            "name, address, phone, birth date."
        )
        if include_political:
            prompt += " Include a political_party field."
        prompt += " Format each entry as JSON."

        # Call the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500  # Adjust for the desired response size
        )

        # Parse the JSON response
        response_text = response['choices'][0]['message']['content']
        data = json.loads(response_text)  # Convert to list of dictionaries
        return data

    except json.JSONDecodeError:
        put_text("Error: Could not parse data from ChatGPT as JSON.")
        return None
    except openai.error.OpenAIError as e:
        put_text(f"OpenAI API error: {e}")
        return None

# Function to output data in the chosen format
def output_data(data, file_format):
    if file_format == 'json':
        return json.dumps(data, indent=4).encode('utf-8')
    elif file_format == 'csv':
        df = pd.DataFrame(data)
        output = BytesIO()
        df.to_csv(output, index=False)
        output.seek(0)
        return output.getvalue()

# PyWebIO interface
def web_interface():
    put_markdown("# Data Creation Application", center=True)

    # User input prompts
    num_entries = input("How many data entries would you like?", type=NUMBER, required=True)
    include_political = radio("Would you like to include political affiliation?", options=['Yes', 'No'], required=True)
    file_format = radio("Choose the output format:", options=['json', 'csv'], required=True)

    include_political = include_political == 'Yes'

    # Generate data
    data = generate_data_with_chatgpt(num_entries, include_political)
    if data is None:
        put_text("Data generation failed. Please try again later.")
        return

    file_data = output_data(data, file_format)
    filename = f"fake_data.{file_format}"

    # Provide a download link
    put_file(filename, file_data, label="Download Data File")

# Start PyWebIO server directly
if __name__ == "__main__":
    start_server(web_interface, port=8080, debug=True)
