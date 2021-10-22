import pyttsx3
import datetime

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)
def date():
    year=int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("today date is")
    speak(date)
    speak(month)
    speak(year)
def wishme():
    speak("welcome back sir")
    time()
    date()
    hour = datetime.datetime.now().hour
    

    if hour>=6 and hour <12:
        speak("good morning bro")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    elif hour >=18 and hour <=24:
        speak("good evening")
    else:
        speak("good night")
        
    speak("im jarvis, how can i help u")
wishme()
    
