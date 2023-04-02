# Offline ChatGPT USSD Application

This is an offline USSD application that allows users to interact with a menu-based system using their mobile phones. The system sends responses via SMS using Africastalking APIs. The application is built using Python and Flask.

## Features

* <b>USSD:</b> The system uses USSD to allow users to send requests. USSD technology allows users to interact with a menu-based system using their mobile phones.
* <b>SMS:</b> The system sends responses via SMS. The user receives the response on their mobile phone.
* <b>Africastalking APIs:</b> The system uses Africastalking APIs to send and receive USSD and SMS messages. Africastalking provides communication APIs that enable developers to integrate messaging, voice, and payments into their applications.

## Requirements

* Python 3.6 or higher
* Flask
* Africastalking account and API key
* Ngrok (for local testing)
* RapidAPI account and API key

## Installation

1. Clone the repository ```git clone https://github.com/GDSC-Karatina-Uni/offline-gpt-with-ussd-sms.git```
2. Create a virtual environment ```python -m venv venv```
3. Activate the virtual environment ```source venv/bin/activate```
4. Install the requirements ```pip install -r requirements.txt```
5. Create a file named ```.env``` and add the following variables:

    ```
    AT_API_KEY=<your api key>
    AT_USERNAME=<your username>

    RAPID_API_KEY=<your rapid api key>
    ```

6. Run the application ```python app.py```
7. Open a new terminal and run ```ngrok http 5000```
8. Copy the https URL and add it to the webhook URL in your Africastalking account
9. Test the application by dialing the USSD code in your Africastalking account

## Usage

The application is a simple chatbot that allows users to interact with it via USSD. The application uses the GPT-3 API to generate responses to the user's messages. The application is built using Python and Flask.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the <a href="https://opensource.org/licenses/MIT">MIT License</a>.
