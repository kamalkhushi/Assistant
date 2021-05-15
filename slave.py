
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
                search=command[(command.index("information on")+len("information on"))+1:]
                print(search+"test")
                information=wikipedia.summary("search")
                print(information)
                talk(information)

            elif ("note" or "make a note") in command:
                    talk("What should i write, senpai")
                    note = give_command()
                    file = open('note.txt', 'w')
                    talk("senpai, Should i include date and time")
                    snfm = continue_command()
                    print(snfm+"hi")
                    if 'yes' in snfm or 'sure' in snfm:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        file.write(strTime)
                        file.write(" :- ")
                        file.write(note)
                    else:
                        file.write(note)
            elif ("roll a dice") in command:
                talk("rolling the dice")
                min = 1
                max = 6
                talk(random.randint(min, max))
    except:
        pass    

while(True):
    run_alexa()
