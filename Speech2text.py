import pyttsx3 
import speech_recognition as sr


def getSpeech():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("say something...!\n")
        audio = r.listen(source)
        try:
            text=r.recognize_google(audio)
            print(f"you said {text}")
        except Exception as e:
            print(e)


getSpeech()