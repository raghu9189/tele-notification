import requests
def sendMessage():
    base_url = "https://api.telegram.org/bot5054588096:AAGcwyf82p9Bw6m6hQ42ZULjdF_l74bcwMU"
    parameters = {"chat_id": "-606084987", "text": "Hello hi"}
    response = requests.get(base_url + "/sendMessage", data = parameters)
sendMessage()
