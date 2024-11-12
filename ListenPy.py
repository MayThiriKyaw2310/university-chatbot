import speech_recognition as sr

#Initialize recognizer
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300 # minimum audio energy to consider for recording
recognizer.dynamic_energy_threshold = True
recognizer.dynamic_energy_adjustment_damping = 0.15
recognizer.dynamic_energy_ratio = 1.5
recognizer.pause_threshold = 0.8 # sec of non-speaking audio  before a phrase is considered complete

recognizer.operation_timeout = None # sec after an internal operation (eg : api request) starts before it times out
recognizer.phrase_threshold = 0.3 # minimum sec of speaking audio before we consider the speaking audi a phase -  value
recognizer.non_speaking_duration = 0.5 #sec of non-speaking auidio to keep both sided of the recording

# def Listen() ->str|None:
def Listen(text=None):
    #use the default microphone as the pytsource
    with sr.Microphone() as source:
        # print("AI Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        #Listen to the user's input
        audio_data = recognizer.listen(source, timeout=5)

        try:
            # print("Recognizing the data...")

            #Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)
            # print(f"Speech Recognized: {text}")
            return text
        
        except sr.UnknownValueError:
            print ("Could not understand the audio, please say it with english!.")
            return None
        
        except sr.RequestError as e:
            print (f"Error: {e}")
            return e
    
    pass
        
# print(str(Listen()))
