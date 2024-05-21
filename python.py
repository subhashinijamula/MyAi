import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki
import pyautogui
x=pyttsx3.init()
import json
import requests
import openai
import pywhatkit as kit
import smtplib as smt
import song
import os
#song.play_song(r"C:\Users\jamul\Downloads\song.mp3")
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiODVkNGI5NTItZTJiOS00NTY3LTliZDQtMzM4YjBhNmRhYjM0IiwidHlwZSI6ImFwaV90b2tlbiJ9.DIFpKgsgy9NdiS1OwrwzvK-WtEVXU_tMPpuPr-zYynk"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "hi! tell meh a joke..!!",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "hasini"
}
def talktoai(query):
    payload["text"]=query
    # print(payload)
    response = requests.post(url, json=payload, headers=headers)
    # print(response.text)
    result=json.loads(response.text)
    speak(result["openai"]["generated_text"])

def speak(audio):
    x.say(audio)
    x.runAndWait()
# speak("Hi I am Itachi AI How can i help you")
def time():
    t=datetime.datetime.now().strftime("%H:%M:%S")
    # print(t)
    speak(t)
# time()
def date():
    y=str(datetime.datetime.now().year)
    m=str(datetime.datetime.now().month)
    d=str(datetime.datetime.now().day)
    speak(d)
    speak(m)
    speak(y)
    # print(y)
# date()
def wish():
    h = datetime.datetime.now().hour
    if h<12:
        speak("Good Morning ")
    elif h>=12 and h<=18:
        speak("Good Afternoon ")
    elif h>18 and h<=21:
        speak("Good Evening")
    else:
        speak("Good Night ")
    speak("How can i help you today")
# str=input()
# wish()
def inp():
    x1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        x1.pause_threshold=1
        audio=x1.listen(source)
        try:
            print("Recognizing...")
            query = x1.recognize_google(audio,language='en-in')
            print(query)
        except Exception as e:
            print(e)
            speak("Can you repeat again")
            inp()
            return "None"
        return query
# inp()
def screenshot():
    im1=pyautogui.screenshot()
    im1.save("C:/Users/jamul/OneDrive/Desktop/ai workshop/img.png")
def youtube(elem):
    kit.playonyt(elem)
def browse(ques):
    kit.search(ques)
def whatsapp(t,msg):
    kit.sendwhatmsg_instantly(t,msg)
def sendemail(to,msg):
    server=smt.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("jamulasubhashini@gmail","hsmn ihoj crxv kevi",)
    server.sendmail("jamulasubhashini@gmail.com",to,msg)
    server.close()
if __name__ =="__main__":
    wish()
    while True:
        query=inp().lower()
        # query=input()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("iam ssummaarizing the wikipedia search")
            query=query.replace("wikipedia", "")
            result= wiki.summary(query,sentences=2)
            print(result)
            speak(result)
        elif "screenshot" in query:
            speak("iam taking screenshot of the screen")
            screenshot()
        elif "exit" in query:
            speak("Exiting")
            print("bye bye")
            exit()
        elif "open youtube" in query:
            speak("what you want to browse ?")
            elem=inp()
            speak("Opening youtube")
            youtube(elem)
        elif "open chrome" in query:
            speak("what do you want to search")
            ques=inp()
            speak("Browsing")
            browse(ques)
        elif "send in whatsapp" in query:
            try:
                speak("input receptent as text")
                t=input()
                speak("say what i want to send")
                msg=inp()
                whatsapp(t,msg)
            except Exception as e:
                print(e)
                speak("failed to send")
        elif "remember" in query:
            speak("what to be remembered")
            data=inp()
            speak("your input is"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()
        elif "speak out data" in query:
            remember=open('data.txt','r')
            speak("the  data i stored is"+remember.read())
        elif "send email" in query:
            try:
                speak("what you want to send")
                msg=inp()
                speak("enter receptient email")
                to=inp()
                sendemail(to,msg)
                speak("it is succcess")
            except Exception as e:
                print(e)
                speak("error")
        elif "play a song" in query:
            song_path=input("enter the song path")
            song.play_song(song_path)
        elif "pause" in query:
            song.control("pause")
        elif "unpause" in query:
            song.control("unpause")
        elif "play" in query:
            try:
                song.play_song(song_path)
            except:
                print("please say play a song")
        elif "stop" in query:
            song.control("stop")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("restart /r /t 1")
        else:
            talktoai(query)
