import requests
def sendMessage():

    parameters = {"chat_id": "-606084987", "text": "Hello hi"}
    response = requests.get(base_url + "/sendMessage", data = parameters)
sendMessage()
