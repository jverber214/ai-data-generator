# ai-data-generator
This Python application uses OpenAI's GPT model to generate fictional datasets and provides a web-based interface for user interaction via PyWebIO. The key features include:

Data Generation: This function creates custom datasets with fields such as name, address, phone, and birth date. An optional field for `political_party` can also be included.

Output Formats: Users can download the generated data as JSON or CSV files.

Interactive Web Interface: The interface prompts users for input parameters such as the number of data entries, whether to include political affiliation, and the desired file format.

Error Handling: Includes robust error handling for OpenAI API responses and JSON parsing.

Environment Configuration: Uses environment variables (via `dotenv`) for secure API key management.

To run the application, execute `python app.py.` This starts a local PyWebIO server and opens the application interface in a web browser(at the following address: 0.0.0.0:8080).

You will need to obtain an OpenAI API Key.  Follow these instructions to do so and insert the key into the code within app.py:

To obtain an OpenAI API key, follow these steps:

1. **Create an OpenAI Account**:
   - Visit the [OpenAI website](https://openai.com/) and click on "Sign Up" if you don't already have an account. If you have an account, log in.

2. **Navigate to the API Section**:
   - Once logged in, go to the OpenAI platform's API management page. This is typically located at [platform.openai.com](https://platform.openai.com/).

3. **Access the API Keys Page**:
   - After logging in, look for the "API Keys" tab in the dashboard menu.

4. **Create a New API Key**:
   - On the API Keys page, click the "Create new secret key" button.
   - A new API key will be generated. Be sure to copy it immediately because this is the only time it will be shown to you.

5. **Store the Key Securely**:
   - Save your API key in a secure location, such as a password manager or a secure environment variable in your development environment. If you lose the key, you will need to generate a new one.

6. **Set Up Billing**:
   - Ensure that you have set up a payment method under the "Billing" section if you plan to use the paid services. Free-tier access may also be available, depending on your usage.

7. **Start Using the API**:
   - Use the API key in your application or scripts to authenticate requests to OpenAI's API services.

### Best Practices:
- Do not share your API key publicly or expose it in your code repositories.
- Use environment variables to manage your API key securely.
- Rotate your API keys periodically for better security.

For further assistance, visit the [OpenAI documentation](https://platform.openai.com/docs/).
