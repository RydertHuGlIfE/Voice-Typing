import pyautogui 
import speech_recognition as sr
import pyttsx3
from time import sleep
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

running = True


while running:
    r=sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening.... ")
        speak("Listening and Ready to type")
        sleep(0.5)
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(mic, duration=0.3)
        audio = r.listen(mic)
        print("Recognising!!!!")
        query = r.recognize_google(audio)
        pyautogui.write(query)
        
else:
    sys.exit()
    


