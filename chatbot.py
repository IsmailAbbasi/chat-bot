from flask import Flask, request, jsonify
from flask import render_template
import json
import time
import random
import wikipedia
from deep_translator import GoogleTranslator
import pyjokes

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
    current_language = data['selected_language']

    if message in ['hello','hi','hola','hey','wassup']:
        bot_response = random.choice([
            'Hello','Hola','Wassup Human'
        ])
    elif message in ['help']:
        bot_response = "Hey i can do multiple tasks : <br> I can play a song for you <br> I can make you laugh by telling you jokes/memes   <br> I can Talk to you in any language you like <br> I can tell about you anything you ask for . <br> I can give you movie suggestions."
    elif message in ['how are you', 'wassup']:
        bot_response = "I am fineeeee."
    elif all(x in message for x in 'who made you'.split(" ")) or all(x in message for x in 'how you born'.split(" ")):
        bot_response = "I was sent to earth by gods of the middle earth <br>.<br>.<br>Abey saale! Kisi Developer ne hi banaya hoga na 😠 <br> maaf krna gusse me thoda idhar udhar nikal jaata hoon "
    # elif all(x in message for x in ['how','are','you']):
    #     bot_response = "I am better then before!"
    elif all(x in message for x in ['what','you','doing']) or all(x in message for x in ['how','you','doing']):
        bot_response = "Trying to do better ;)<br>(Spiderman reference)"
    elif all(x in message for x in ['who','are','you']) or all(x in message for x in ['how','you','doing']):
        bot_response = "I am Ultron chat bot made by Iron man <br> Not by Tony Stark <br> by Ismail Abbasi"
    elif all(x in message for x in ['who','is','ismail']) or all(x in message for x in ['tell','about','ismail']):
        bot_response = "Ismail Abbasi is a studying CS from Jamia hamdard delhi you can find more about "
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

    elif message.startswith("talk to me in"):
        language = message.replace("talk to me in ", "")
        response_type = 'change_langauge'
        action = language
        current_language = language
        bot_response = "Ok! From now on I will talk to you in " + language.title() + "."

    elif all(x in message for x in ['tell','me','a','joke',]) or all(x in message for x in ['tell','me','a','meme']) or all(x in message for x in ['make','me','laugh']): 
    # message.startswith("meme") or message.startswith("tell me a joke") or message.startswith("make me laugh") or message.startswith("joke"):
        # topic = message.replace("meme", "").replace("tell me a joke", "").replace("make me laugh","").replace("can you tell me a", "")
        bot_response = pyjokes.get_joke()  
        # bot_response = print(pyjokes.get_joke())

    if current_language != 'english':
        translator = GoogleTranslator(source='auto', target=current_language)
        bot_response = translator.translate(bot_response)
        

    response = {"response":bot_response, "response_type":response_type, "action":action}
    return jsonify(response)


    
if __name__  == '__main__':
    app.run(debug=True)