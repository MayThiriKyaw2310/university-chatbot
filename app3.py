from flask import Flask, render_template, request, jsonify
from Chat import Chat
from SpeakOffline import Speak
from Ocr import Ocr
from Basic import ChromeCode
from test import KnowApps
from Filter import Filter
import pygetwindow as gw
from os import getcwd
import base64
from ListenPy import Listen
import keyboard
import time
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
# CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
# Global variable to track the stop state
is_listening = True

#@app.route('/')
#def index():
#  return render_template('ECbot_2.html')


@app.route('/stop', methods=['POST'])
def stop():
    global is_listening
    is_listening = False
    return jsonify({'message': 'Stopped'}), 200

@app.route('/postdata', methods=['POST'])
def post_data():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            Q = data["text"]
            LQ = len(Q.split(" "))
            CURRENT_APP = ""
            Output = ""
            reply = ""
            try:
                CURRENT_APP = gw.getActiveWindowTitle()
            except:
                CURRENT_APP = ""
            CURRENT_APP_NAME = CURRENT_APP.split(" - ")[-1]

            if "open chrome" in Q.lower():
                keyboard.press_and_release("Ctrl + n")
                reply = "Opening Chrome"
                Speak(reply)
                Listen()  # Call Listen without arguments
            
            elif "open youtube" in Q.lower():
                # Simulate opening Chrome
                keyboard.press_and_release("Ctrl + n")  # Open a new window
                time.sleep(2)  # Wait for Chrome to open

                # Simulate typing the YouTube URL and pressing Enter
                keyboard.write("https://www.youtube.com")
                keyboard.press_and_release("Enter")
                
                reply = "Opening YouTube"
                Speak(reply)
                Listen()  # Call Listen without arguments

            elif "google" in Q.lower():
                search_query = Q.lower().replace("google", "").strip()

                keyboard.press_and_release("Ctrl + n")
                time.sleep(2)
                keyboard.press_and_release("Ctrl + t")
                time.sleep(1)

                keyboard.write("https://www.google.com")
                keyboard.press_and_release("Enter")
                time.sleep(2)

                keyboard.write(search_query)
                keyboard.press_and_release("Enter")

                reply = f"Searching for '{search_query}' in Chrome"
                Speak(reply)
                Listen()
            
            else:
                if Q is not None:
                    Q = Q.lower().strip()
                    SQ = Q.split(" ")[0]
                    if (SQ == "click" or (SQ == "double" and "click" in Q)) and LQ < 7:
                        Q = Q.replace("click", "")
                        Q = Q.replace("on", "")
                        Q = Q.replace("helper", "")
                        Q = Q.replace("double", "")
                        Q = Q.replace("button", "")
                        reply = Ocr(Q.strip())
                        Speak(reply)
                        Listen(Output)  # If Listen requires an argument, use Output
                    elif CURRENT_APP_NAME in KnowApps:
                        Func_ = KnowApps[CURRENT_APP_NAME]
                        Output = Func_(Q)
                        if Output != False:
                            keyboard.press_and_release(Output)
                        else:
                            reply, confidence = Chat(Q)
                            if confidence > 0.2:
                                Speak(reply)
                                Listen()
                            else:
                                reply = "Sorry, I didn't understand that."
                                Speak(reply)
                                Listen()
                    else:
                        reply, confidence = Chat(Q)
                        if confidence > 0.2:
                            Speak(reply)
                            Listen()
                        else:
                            reply = "Sorry, I didn't understand that."
                            Speak(reply)
                            Listen(Output)  # If Listen requires an argument, use Output
                else:
                    reply = "Say Something"
                    Speak(reply)
                    Listen(Output)  # If Listen requires an argument, use Output

            new = f"{getcwd()}\\temp\\temp_audio.mp3"
            with open(new, 'rb') as mp3_file:
                audio = base64.b64encode(mp3_file.read()).decode('utf-8')

            response_data = {"audio": audio, "speak": reply, "listen": Q}

            return jsonify(response_data), 200
        else:
            return jsonify({'error': 'Invalid Content-Type. Expected application/json'}), 400
    else:
        return jsonify({'error': 'Method not allowed'}), 405


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)
                    