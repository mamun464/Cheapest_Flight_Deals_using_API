import os
import vonage

# This class is responsible for sending notifications with the deal flight details.


def sms_sent(Msg_body):
    client = vonage.Client(key="44cfe8f9", secret="3rEDEK5PH5uUL9HN")
    sms = vonage.Sms(client)

    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": "8801767213613",
            "text": Msg_body,
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

sms_sent("Testing mgs")