
from __future__ import print_function
from decouple import config

import africastalking
import requests

from flask import Flask, request
import africastalking
# sqlite3
import sqlite3
from flask import g


class SMS:
    def __init__(self):
        # Set your app credentials
        self.username = config('AT_USERNAME')
        self.api_key = config('AT_API_KEY')

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self, message, phone_number):
        # Set the numbers you want to send to in international format
        recipients = [f"{phone_number}"]

        # Set your message
        message = message

        # Set your shortCode or senderId
        sender = "sandbox"
        try:
            # Thats it, hit send and we'll take care of the rest.
            response = self.sms.send(message, recipients)
            print(response)
        except Exception as e:
            print('Encountered an error while sending: %s' % str(e))


"""
USSD Flask app using Africas Talking API
We will create a simple USSD app that will facilitate the use of OpenAI offline
"""


# Initialize the SDK
username = "sandbox"    # use 'sandbox' for development in the test environment

# membership table

app = Flask(__name__)

response = ""

@app.route('/ussd/', methods=['POST', 'GET'])
def ussd_callback():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == "":
        # This is the first request. Note how we start the response with CON
        response = "CON Welcome to OpenAI USSD\n"
        response += "1. Enter What you want to know\n"
        response += "2. Exit\n"
        response += "3. Main Menu"

    elif text == "1":
        # let the user type in the question
        response = "CON Enter your question"

    elif text == "2":
        # let the user type in the question
        response = "END Thank you for using OpenAI USSD"

    elif text == "3":
        # let the user type in the question
        response = "CON Welcome to OpenAI USSD\n"
        response += "1. Enter What you want to know\n"
        response += "2. Exit\n"
        response += "3. Main Menu"

    else:
        # if the user types in the question
        if text != "":
            # send the question to the openai api
            url = "https://openai80.p.rapidapi.com/chat/completions"

            payload = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {
                        "role": "user",
                        "content": text
                    }
                ]
            }
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": config('RAPID_API_KEY'),
                "X-RapidAPI-Host": "openai80.p.rapidapi.com"
            }

            response = requests.request("POST", url, json=payload, headers=headers)

            # print the answer to the question
            answer = response.json()["choices"][0]["message"]["content"]
            response = "CON Check your phone for the answer\n"
            response += "1. Enter What you want to know\n"
            response += "2. Exit\n"
            response += "3. Main Menu"

            SMS().send(answer, phone_number)
        
    # Print the response onto the page so that our gateway can read it
    return response


if __name__ == '__main__':
    
    app.run(debug=True)






































# if __name__ == '__main__':
#     SMS().send(answer)

