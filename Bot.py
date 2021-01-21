import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import os
eng = pyttsx3.init('sapi5')
voices = eng.getProperty('voices')


def speak(audio):
    eng.say(audio)
    eng.runAndWait()

def Greet():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12 :
        speak("Good Morning")
    elif hour >=12 and hour<18 :
        speak("Good Afternoon")
    else :
        speak("Good Evening")
    speak("I Am Jarvis Sir.How can I help you?")

def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said :{query}\n")
    except Exception as e:
        #print(e)
        print("Say that Again Please!!")
        return "None"
    return query

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sender's email id','sender's password')
    server.sendmail('dasshamik20@gmail.com',to,content)
    server.close()
if __name__ == "__main__":
    Greet()

    while True:
        query = take().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wkipedia')
            print(results)
            speak(results)
        elif "open youtube" in query :
            webbrowser.open("youtube.com")
        elif "open amazon" in query:
            webbrowser.open("amazon.com")
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir='F:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif "email to shamik" in query :
            try :
                speak("What should I say ?")
                content=take()
                to = "dasshamik18@gmail.com"
                sendemail(to, content)
                speak("Email has been sent Sir")
            except Exception as e:
                print(e)
                speak("Sorry Sir Cannot send your email")



