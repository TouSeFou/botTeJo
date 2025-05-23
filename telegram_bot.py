import requests
import schedule
import time
import os

# Token et ID utilisateur Telegram
import os

TOKEN = os.environ['TELEGRAM_TOKEN']
USER_ID = os.environ['TELEGRAM_USER_ID']


# Récupérer une blague depuis JokeAPI
def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?lang=fr", verify=True)
    joke_data = response.json()
    message= f"{joke_data['setup']}\n {joke_data['delivery']}"
    return message

# Récupérer une citation depuis ZenQuotes
def get_quote():
    response = requests.get("https://zenquotes.io/api/random" , verify=True)
    quote_data = response.json()
    return quote_data[0]["q"] + " -" + quote_data[0]["a"]

# Envoyer un message via Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": USER_ID,
        "text": message
    }
    return requests.post(url, data=payload, verify=True)

# Combiner blague + citation et envoyer
def send_joke_and_quote():
    joke = get_joke()
    quote = get_quote()
    message = f"🤖 Blague du jour:\n{joke}\n\n💡 Citation du jour:\n{quote}"
    reponse = send_telegram_message(message)
    print("Success:", reponse.ok)
    print("Status Code:", reponse.status_code)
    print("Response Text:", reponse.text)
    # if(reponse['ok']==True):
    #     print(f" le message : {message} sent 👌")

send_joke_and_quote()