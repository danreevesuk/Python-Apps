import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import playsound
from GoogleNews import GoogleNews
import subprocess



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.setProperty("rate" , 140)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello, I am Jarvis. how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout= 100)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:   
        print("Say that again please...")  
        return ""
    return query

def Wake_Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Call to wake me up")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout= 100)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:   
        print("You have failed to trigger me...")
        speak("Intruder!!! Going offline now.. good bye")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('zohaibscorpion167@gmail.com', 'zohaibisthebest')
    server.sendmail('zohaibscorpion167@gmail.com', to, content)
    server.close()
    
    
def note(query):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(os.path.join('H:\\Python\\notes\\',file_name), "w") as f:
        f.write(query)




def start_func():
    while True:
        query = takeCommand().lower()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                speak("What do you want to search?")
                query = takeCommand()
                print('Searching Wikipedia... Please Wait')
                speak('Searching Wikipedia... Please Wait')
                results = wikipedia.summary(query, sentences=1)
                print("According to Wikipedia: "+ results)
                speak("According to Wikipedia"+results)
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to find this on wikipedia")
            
            
        elif "what can you do" in query or "what you can do" in query:              
            speak("I can do many tasks for you... ")
            speak("I can play a song or open facebook and youtube... I can read news headlines for you Sir!")
            speak("I can also send emails... or if you want to search any thing on google and wikipedia... i can also do it for you")
            
        elif 'news' in query:
            try:
                speak("Which topic would you like to hear")
                query = takeCommand()
                print('Scrapping news for you... Please Wait')
                speak('Scrapping news for you... Please Wait')
                googlenews = GoogleNews()
                googlenews = GoogleNews('en','d')
                googlenews.search(query)
                googlenews.result()
                news = googlenews.gettext()
                print(news)
                speak(news)
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to find news on this topic")
        

        
        elif 'google' in query:
            try:
                speak("What do you want to search?")
                query = takeCommand()
                print('Searching Google... Please Wait')
                speak('Searching Google... Please Wait')
                results = webbrowser.open("https://www.google.com/search?q="+(query))
                speak('Opening Google...')
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to find this on google")
            

            
            
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")


        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com") 
            
        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")  


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")    
            speak("Sir, the time is " +(strTime))
        
        elif 'date' in query:
            current_date = datetime.date.today().strftime("%d/%m/%Y")
            speak(current_date)


        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "leatherwonderus@gmail.com"   
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")
                
        elif 'how are you' in query:
            speak("I am always good Sir, Thanks for asking... now a days people dont really ask this from a machine... haa haa")
            
        elif 'your name' in query:
            speak("My name is jarvis, an AI assistant!")
            
        elif 'song' in query:
            playsound.playsound('snowmen.mp3')
            
        elif "remember this" in query or "make a note" in query or "write down" in query :
            speak("What would you like me to remember?")
            query = takeCommand()
            note(query)
            print("Making a note for you")
            speak("I've made a note of that.")
            
        elif "open the notes" in query or "open notes" in query or "my notes" in query:
            os.startfile("H:\\Python\\notes")
                    
                
        elif "stop now" in query or "goodbye" in query:
            speak("Come again good byeee")
            break 
    
        
        
                
if __name__ == "__main__": 
    query = Wake_Command().lower()
    if "wake up" in query: 
        wishMe()
        start_func()
    else:
        print("You have failed to trigger me...")
        speak("Intruder!!! Going offline now.. good bye")
    