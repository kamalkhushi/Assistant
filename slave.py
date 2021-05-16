import pyttsx3
import speech_recognition as sr
import pyaudio
import os
import wolframalpha
import pywhatkit
import datetime
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
#import winshell
#import pyjokes
#import feedparser
import bs4
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
#from clint.textui import progress
#from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

listener=sr.Recognizer()
speaker=pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice',voices[0].id)
speaker.setProperty("rate",160)
continuescommand=""

def talk(text):
    speaker.say(text)
    speaker.runAndWait()

def give_command():
    try:
        with sr.Microphone() as mic:
            voice = listener.listen(mic)
            command=listener.recognize_google(voice)
            command = command.lower()        
    except:
        pass
    return command

def continue_command():
    store=give_command()
    return store

def run_alexa():
    min = 0
    try:
        command=give_command()
        print(command)
        if 'kamal' in command:
            command= command[(command.index("kamal")+len("kamal"))+1:]
            print(command)
            if 'play' in  command:
                song=command.replace('play',"")
                talk('playing' + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time=datetime.datetime.now().strftime('%#I %M %p')
                print(time)
                talk('current time is' +time)
            elif 'date' in command:
                date=datetime.datetime.now().strftime("%B %d %Y")
                print(date)
                talk(date)
            elif "information on" in command:
                people=command[(command.index("information on")+len("information on"))+1:]
                information=wikipedia.summary(people,1)
                talk(information)
            elif "good morning" in command:
                say = ["Good Morning! How are you Senpai","Good Morning!, have a nice day Senpai","Good Morning! I am at your service Senpai"]
                max = len(say)-1
                talkformat=random.randint(min, max)
                talk(say[talkformat])
            elif "good evening" in command:
                say = ["Good evening! How are you Senpai","Good evening!, have a nice day Senpai","Good evening! I am at your service Senpai"]
                max = len(say)-1
                talkformat=random.randint(min, max)
                talk(say[talkformat])
            elif "good night" in command:
                say = ["Good night! take care Senpai","Good night!, See you later Senpai","Good night! Bye Senpai","Good night! see you later Senpai"]
                max = len(say)-1
                talkformat=random.randint(min, max)
                talk(say[talkformat])  
                exit()  
            elif "take notes" in command or "make a note" in command:
                    say = ["What should i write?, senpai!","What should i Note Down?, senpai!","Senpai ,Im noting down?"]
                    max = len(say)-1
                    talkformat=random.randint(min, max)
                    talk(say[talkformat])
                    note = give_command()
                    file = open('note.txt', 'w')
                    talk("senpai, Should i include date and time")
                    reply = continue_command()
                    if 'yes' in reply or 'sure' in reply or "yea" in reply or "ok" in reply or "alright" in reply or "yeah" in reply or "cool" in reply or "okay" in reply:
                        time = datetime.datetime.now().strftime("%#I:%M %p")
                        date=datetime.datetime.now().strftime("%B %d %Y")
                        file.write(time)
                        file.write(" :- ")
                        file.write(note)
                    else:
                        file.write(note)

            elif "read notes" in command or "read note" in command:
                talk("reading Notes")
                file = open("note.txt", "r")
                talk(file.read())

            elif "roll a dice" in command:
                talk("rolling the dice")
                min = 1
                max = 6
                talk(random.randint(min, max))
            elif 'shutdown system' in command or 'turn off the system' in command or 'shutdown' in command:
                talk("Hold On a Sec ! Your system is on its way to shut down")
                os.system("shutdown /s /t 1")
    except:
        pass    

while(True):
    run_alexa()
