import pyttsx3

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')

engine.setProperty('rate', 200)
engine.setProperty('voice', voice[1].id)

temp_audio_path = 'temp//temp_audio.mp3'
def Speak(*args, **kwargs):
    audio = ""
    for i in args:
        audio += str(i)
        # print(audio)
    # engine.say(audio)
    engine.save_to_file(audio, temp_audio_path)
    engine.runAndWait()
#     return temp_audio_path
# Speak("hi Goodmorning", "Myanmar",)