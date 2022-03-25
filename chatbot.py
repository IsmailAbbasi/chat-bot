from flask import Flask, request, jsonify
from flask import render_template
import json
import time
import random
import wikipedia

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/send-msg/", methods=['POST'])
def send_message():
    time.sleep(1)
    data = json.loads(request.data)
    message = data['message'].lower().replace("?","").replace(".","").replace("!","")
    bot_response = "Sorry, I didn't get that!"
    response_type = 'text'
    action = ''

    if message in ['hello','hi','hola','hey','wassup']:
        bot_response = "Heya dawg!"
    elif message in ['how are you', 'wassup']:
        bot_response = "I am fine."
    elif all(x in message for x in ['how','are','you']):
        bot_response = "I am better then before!"
    elif all(x in message for x in ['what','you','doing']):
        bot_response = "Trying to do better ;)<br>(Spiderman reference)"
    elif all(x in message for x in ['play','song']):
        bot_response = 'Playing a random song on youtube from my favourite playlist'
        response_type = 'open_link'
        action = random.choice([
            "https://www.youtube.com/watch?v=wrj3cwnt2CY",
            "https://www.youtube.com/watch?v=RUidyVbkQkk",
        ])
    elif message.startswith("define") or message.startswith("what is") or message.startswith("tell me about") or message.startswith("who is"):
        topic = message.replace("define", "").replace("what is", "").replace("tell me about","").replace("who is", "")
        try:
            bot_response = wikipedia.summary(topic)
        except:
            bot_response = "Sorry, I don't know anything about " + topic + "!"

    response = {"response":bot_response, "response_type":response_type, "action":action}
    return jsonify(response)

    
if __name__  == '__main__':
    app.run(debug=True)