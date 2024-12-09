import openai
import os
from pywebio import start_server
from pywebio.output import put_file, put_text, put_html
from pywebio.input import input, radio, NUMBER
from io import BytesIO
from dotenv import load_dotenv
from openai import OpenAIError
import pandas as pd
import json

# Ensure API key is set
load_dotenv()  # Loads environment variables from .env
openai_api_key = os.getenv("sk-proj-your-project-key")

# Function to generate data with error handling
def generate_data_with_chatgpt(num_entries, include_political):
    try:
        # Construct a strict JSON output prompt
        prompt = (
            f"Generate {num_entries} entries of fictional data. Each entry should be a JSON object "
            f"with the following fields: 'name', 'address', 'phone', 'birth_date'."
        )
        if include_political:
            prompt += " Include a field named 'political_party'."
        prompt += (
            " Respond strictly with a JSON array of objects. Do not include any explanations or other text."
        )

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Adjust model as needed
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000  # Allow enough tokens for larger datasets
        )

        # Parse the response content
        response_text = response['choices'][0]['message']['content']
        data = json.loads(response_text)  # Convert response to Python list/dict
        return data

    except json.JSONDecodeError as e:
        # Log response for debugging purposes
        print("Raw response from ChatGPT:", response['choices'][0]['message']['content'])
        put_text("Error: Could not parse data from ChatGPT as JSON. Please refine the input.")
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
    put_html("<h1 style='text-align: center;'>Data Creation Application</h1>")

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
# Run the app.py file in the terminal with the command python app.py. This will start the PyWebIO server and open a new tab in your web browser with the application interface. You can then interact with the application to generate and download the fictional data.


