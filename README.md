# ai-data-generator
This Python application uses OpenAI's GPT model to generate fictional datasets and provides a web-based interface for user interaction via PyWebIO. The key features include:

Data Generation: This function creates custom datasets with fields like `name,` `address,` `phone,` and `birth_date.` An optional field for `political_party` can also be included.

Output Formats: Users can download the generated data as JSON or CSV files.

Interactive Web Interface: A user-friendly interface prompts users for input parameters such as the number of data entries, whether to include political affiliation, and the desired file format.

Error Handling: Includes robust error handling for OpenAI API responses and JSON parsing.

Environment Configuration: Uses environment variables (via `dotenv`) for secure API key management.

Execute `python app.py` to run the application. This starts a local PyWebIO server and opens the application interface in a web browser.
