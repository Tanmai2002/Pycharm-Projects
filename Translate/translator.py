import speech_recognition as sr
from textblob import TextBlob
from gtts import gTTS
from playsound import playsound
from google_trans_new import google_translator
def list():
    li=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        li.adjust_for_ambient_noise(source)
        audio=li.listen(source)
    try:
            print("Recognizing..")
            query=li.recognize_google(audio)
            ryal=google_translator().translate(query,lang_tgt='te')
            tp=gTTS(ryal)
            tp.save('trial.mp3')
            playsound('trial.mp3')


            print(f"User said :{query},{TextBlob(query).detect_language()}")
    except Exception as e:
            print("Error",e)


list()