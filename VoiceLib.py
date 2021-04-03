import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hey Smarty, How may i help you!")


def takecommand():
    ''' Takes Input from Microphone'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening. . . . ")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}")

    except Exception as e:
        print("Say that again")
        return "None"
    return query


def sendemail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", 'your-password')
    server.sendemail('youremail@gmail.com', to, content)
    server.close()


def cycle():
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            # webbrowser.Chrome("google.com")
            webbrowser.open("google.com")
        elif 'open coursera' in query:
            webbrowser.open("coursera.org")
        elif 'play music' in query:
            music_location = 'D:\\Coding\\Coding in Py\\Py Proj\\RMX Voice\\Songs'
            songs = os.listdir(music_location)
            print(songs)
            os.startfile(os.path.join(music_location, songs[0]))
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Hey Smartee , the Time is {str_time}")
        elif 'open code' in query:
            vsc_loc = '"D:\\Microsoft VS Code\\Code.exe"'
            os.startfile(vsc_loc)
        elif 'brave' in query:
            vsc_loc01 = '"C:\\Users\\Public\\Desktop\\Brave"'
            os.startfile(vsc_loc01)
        elif 'teams' or 'meeting' in query:
            vsc_loc02 = '"C:\\Users\\Ritish Mohapatra\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams"'
            os.startfile(vsc_loc02)
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
            # vsc_loc = '"D:\\Microsoft VS Code\\Code.exe"'
            # os.startfile(vsc_loc)
        elif 'Bye' or 'exit' or 'bye rmx' in query:
            speak("Thanks for giving me your valuable time")
            exit() 
        elif 'email to sender' in query:
            try:
                speak("What Should I Say")
                content = takecommand()
                # sendemail=(to,content)
                speak("Email Sent")
            except Exception as e:
                print(e)
                speak("Email cannot be sent")