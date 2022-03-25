from flask import Flask, request, jsonify
from flask import render_template
import json
import time

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

    if message in ['hello','hi','hola','hey','wassup']:
        bot_response = "Heya dawg!"
    elif message in ['how are you', 'wassup']:
        bot_response = "I am fine."

    response = {"response":bot_response}
    return jsonify(response)

    
if __name__  == '__main__':
    app.run(debug=True)