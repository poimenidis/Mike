import sys
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if(hour>=0 and hour < 12):
        speak("Good Morning sir!")
    elif (hour > 12 and hour < 18):
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")

    speak("I am Mike! Please tell me how i may help you! Just call my name...")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=5)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognition...")
        query = r.recognize_google(audio, language='en-gr')
        print("User said: "+ query)

    except Exception as e:
        print("Sorry...Can you repeat please?")
        return "None"

    return query

def get_weather(city):
    try:
        weather_key = "79daad292e6f1860ac9c3bac50f12d64"
        url = "https://api.openweathermap.org/data/2.5/forecast"
        params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
        response = requests.get(url, params=params)
        weather = response.json()
        print(weather)
        name = city.title()
        try:
            for i in range(0, 1):
                desc = weather['list'][i]['weather'][0]['description']
                temp = weather['list'][i]['main']['temp']
                speak("the weather in " + str(name) + " is "+ str(desc)+ "and the temperature is "+str(temp))
        except:
            speak('Sorry')
    except:
        speak('Sorry')


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        #About Mike
        if 'mike' in query and  'how are you' in query:
            speak("I am fine thank you")
        elif 'mike' in query and 'who are you' in query:
            speak("I am Mike, your personal assistant")
        elif 'mike hello' == query or 'hello mike' == query or 'mike hi' == query or 'hi mike' == query:
            speak("Hello sir")
        elif 'mike' in query and 'thank you' in query:
            speak("You're welcome sir")
        elif 'mike' in query and "what's up" in query:
            speak("just chillin bro")

        #Wikipedia searching
        elif 'mike' in query and  'wikipedia' in query:
            speak('I am searching Wikipedia...')
            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("Sorry...I couldn't find something relevant in wikipedia?")

        #open browser
        elif 'mike' in query and  "open" in query and "youtube" in query:
            speak("Yes sir... just a moment")
            webbrowser.get(chrome).open("youtube.com")
        elif 'mike' in query and "open" in query and "google" in query:
            speak("Yes sir... just a moment")
            webbrowser.get(chrome).open("google.com")
        elif 'mike' in query and "open" in query and "news" in query:
            speak("Yes sir... just a moment")
            webbrowser.get(chrome).open("england365.gr")
        elif 'mike' in query and "open" in query and "my emails" in query:
            speak("Yes sir... just a moment")
            webbrowser.get(chrome).open("https://accounts.google.com/AccountChooser/signinchooser?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&hl=el&flowName=GlifWebSignIn&flowEntry=AccountChooser")
        elif 'mike' in query and "open" in query and "facebook" in query:
            speak("Yes sir... just a moment")
            webbrowser.get(chrome).open("facebook.com")
        elif 'mike' in query and "open" in query and "instagram" in query:
            speak("Yes sir... just a moment")
            webbrowser.get(chrome).open("instagram.com")
        elif 'mike' in query and "open" in query and "android console" in query:
            speak("Yes sir... just a moment")
            webbrowser.get(chrome).open("https://play.google.com/apps/publish/?account=6059930594737099253")
        elif 'mike' in query and "open" in query and ("my portfolio" in query or "my site" in query):
            speak("Yes sir... just a moment")
            webbrowser.get(chrome).open("https://my-portfolio-240608.appspot.com/")
        elif 'mike' in query and "open" in query and "skroutz" in query:
            speak("Yes sir... just a moment")
            webbrowser.get(chrome).open("skroutz.gr")
        elif 'mike' in query and 'open' in query and "highlights" in query:
            speak("Yes sir... just a moment")
            webbrowser.get(chrome).open("https://ourmatch.net/")

        #world
        elif 'mike' in query and 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, The time is " + strTime)
        elif 'mike' in query and 'weather' in query:
            get_weather("thessaloniki")

        #open apps
        elif 'mike' in query and 'open' in query and 'android studio' in query:
            path = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(path)
            speak("Yes sir... just a moment")
        elif 'mike' in query and 'open' in query and 'pycharm' in query:
            path = "C:\\Program Files\\JetBrains\\PyCharm 2018.3.5\\bin\pycharm64.exe"
            os.startfile(path)
            speak("Yes sir... just a moment")
        elif 'mike' in query and 'open' in query and 'chrome' in query:
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
            speak("Yes sir... just a moment")
        elif 'mike' in query and 'open' in query and 'bitdefender' in query:
            path = "C:\\Program Files\\Bitdefender Antivirus Free\\bdagent.exe"
            os.startfile(path)
            speak("Yes sir... just a moment")
        elif 'mike' in query and 'open' in query and 'intelj' in query:
            path = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2019.1.2\\bin\\idea64.exe"
            os.startfile(path)
            speak("Yes sir... just a moment")
        elif 'mike' in query and 'open' in query and 'cleaner' in query:
            path = "C:\\Program Files\\CCleaner\\CCleaner64.exe"
            os.startfile(path)
            speak("Yes sir... just a moment")
        elif 'mike' in query and 'open' in query and 'photoshop' in query:
            path = "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe"
            os.startfile(path)
            speak("Yes sir... just a moment")
        elif 'mike' in query and 'open' in query and 'battleship' in query:
            path = "C:\\Users\\konst\\Documents\\Προγραμματισμος\\Java\\BattleShip\\BattleShip\\BattleShip_V2.2.exe"
            os.startfile(path)
            speak("Yes sir... just a moment")
        elif 'mike' in query and 'open' in query and ('word' in query or 'world' in query):
            path = "C:\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007"
            os.startfile(path)
            speak("Yes sir... just a moment")
        elif 'mike' in query and 'open' in query and ('exel' in query or 'excel' in query):
            path = "C:\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007"
            os.startfile(path)
            speak("Yes sir... just a moment")

        # close apps
        elif 'mike' in query and 'close' in query and 'android studio' in query:
            speak("Yes sir... just a moment")
            os.system("TASKKILL /F /IM studio64.exe")
        elif 'mike' in query and 'close' in query and 'pycharm' in query:
            speak("Yes sir... just a moment")
            os.system("TASKKILL /F /IM pycharm64.exe")
        elif 'mike' in query and 'close' in query and 'chrome' in query:
            speak("Yes sir... just a moment")
            os.system("TASKKILL /F /IM chrome.exe")
        elif 'mike' in query and 'close' in query and 'intelj' in query:
            speak("Yes sir... just a moment")
            os.system("TASKKILL /F /IM idea64.exe")
        elif 'mike' in query and 'close' in query and 'photoshop' in query:
            speak("Yes sir... just a moment")
            os.system("TASKKILL /F /IM Photoshop.exe")
        elif 'mike' in query and 'close' in query and 'battleship' in query:
            speak("Yes sir... just a moment")
            os.system("TASKKILL /F /IM javaw.exe")
        elif 'mike' in query and 'close' in query and ('exel' in query or 'excel' in query):
            speak("Yes sir... just a moment")
            os.system("TASKKILL /F /IM EXCEL.EXE")

        #windows
        elif 'mike' in query and 'restart' in query and 'my pc' in query:
            speak("Yes sir... just a moment")
            os.system("shutdown -t 0 -r -f")
        elif 'mike' in query and ('shut down' in query or "turn off" in query) and 'my pc' in query:
            speak("Yes sir... just a moment")
            os.system('shutdown -s')
        elif 'mike' in query and 'sleep' in query:
            speak("Bye Bye sir")
            sys.exit(0)

        elif 'mike' in query:
            speak("Sorry sir, can you repeat it please?")


