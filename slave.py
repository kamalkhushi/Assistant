import pafy
import vlc
import youtube_dl
import speech_recognition as sr
import pyaudio
import os
import pywhatkit
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import re
import random
import operator
import datetime
import wikipedia
import webbrowser
import smtplib
import ctypes
import time
import requests
import shutil
from youtubesearchpython import VideosSearch
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
from gogoanimeapi import gogoanime as anime
import sphinx

listener=sr.Recognizer()
speaker=pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice',voices[0].id)
speaker.setProperty("rate",160)
continuescommand=""
Instance = vlc.Instance()
player = Instance.media_player_new()
player.audio_set_volume(30)
def talk(text):
    speaker.say(text)
    speaker.runAndWait()

#Full command
def give_command():
    try:
        with sr.Microphone() as mic:
            voice = listener.listen(mic)
            command=listener.recognize_google(voice,language='en-in')
            command = command.lower()        
    except:
        pass
    return command

#continues command
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

        #play song
            if 'play' in  command:
                try:
                    song=command.replace('play',"")
                    talk('playing' + song)
                    videosSearch = VideosSearch(song, limit = 1)                  
                    data=videosSearch.result()
                    for name in data['result']:
                        name=name['link']
                    video = pafy.new(name)
                    bestaudiost = video.getbestaudio()
                    playurl = bestaudiost.url
                    Media = Instance.media_new(playurl)
                    Media.get_mrl()
                    player.set_media(Media)
                    player.play()
                except:
                    talk("Im sorry,I have to play this song on browser")
                    pywhatkit.playonyt(name)

        #ask time
            elif 'time' in command:
                time=datetime.datetime.now().strftime('%#I %M %p')
                print(time)
                talk('current time is' +time)

        #ask date
            elif 'date' in command:
                date=datetime.datetime.now().strftime("%B %d %Y")
                print(date)
                talk(date)

        #ask time information on
            elif "information on" in command:
                people=command[(command.index("information on")+len("information on"))+1:]
                information=wikipedia.summary(people,1)
                talk(information)

        #ask wishes
            elif "good morning" in command:
                say = ["Good Morning! How are you Senpai","Good Morning!, have a nice day Senpai","Good Morning! I am at your service Senpai"]
                max = len(say)-1
                talkformat=random.randint(min, max)
                talk(say[talkformat])
        
        #ask wishes
            elif "good evening" in command:
                say = ["Good evening! How are you Senpai","Good evening!, have a nice day Senpai","Good evening! I am at your service Senpai"]
                max = len(say)-1
                talkformat=random.randint(min, max)
                talk(say[talkformat])

        #ask wishes
            elif "good night" in command:
                say = ["Good night! take care Senpai","Good night!, See you later Senpai","Good night! Bye Senpai","Good night! see you later Senpai"]
                max = len(say)-1
                talkformat=random.randint(min, max)
                talk(say[talkformat])  
                exit()  
            
        #ask take notes
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
            
            #ask read notes
            elif "read notes" in command or "read note" in command:
                talk("reading Notes")
                file = open("note.txt", "r")
                talk(file.read())


            #ask roll a dice
            elif "roll a dice" in command:
                talk("rolling the dice")
                min = 1
                max = 6
                talk(random.randint(min, max))

            #ask shutdown system
            elif 'shutdown system' in command or 'turn off the system' in command or 'shutdown' in command:
                talk("Hold On a Sec ! Your system is on its way to shut down")
                os.system("shutdown /s /t 1")

            #ask restart pc
            elif 'restart pc' in command or 'reboot pc' in command or 'restart the computer' in command:
                talk("Hold On a Sec ! Your system is on its way to restart")
                os.system("shutdown /r /t 1")

            #ask lock my pc
            elif "lock my pc" in command or "lock the pc" in command :
                ctypes.windll.user32.LockWorkStation()

            #ask stop
            elif "stop" in command :
                player.stop()

            #ask pause
            elif "pause" in command or "pause the song" in command or "pause the music" in command or "resume" in command or "resume the song" in command or "resume the music" in command or "resume song" in command or "resume music" in command or "pause song" in command or "pause music" in command or "hold on" in command or "hold" in command or "continue" in command or "wait" in command:
                player.pause()


            #ask volume settings
            elif "lower volume" in command or "reduce volume" in command or "increase volume" in command or "raise volume" in command or "volume" in command:
                x = re.findall('[0-9]+', command)
                player.audio_set_volume(int(x[0]))

            #ask Heads or tails
            elif "flip a coin" in command or "toss" in command or "heads or tails" in command:
                max=1
                heads_or_tails=["heads","tails"]
                current=random.randint(min, max)
                talk(heads_or_tails[current])
            
            #ask to play video
            elif "video on" in command or "youtube" in command:
                try:
                    song=command.replace('play',"")
                    talk('playing' + song)
                    player.audio_set_volume(50)
                    videosSearch = VideosSearch(song, limit = 1)                  
                    data=videosSearch.result()
                    for name in data['result']:
                        name=name['link']
                    video = pafy.new(name)
                    bestaudiost = video.getbestaudio()
                    playurl = bestaudiost.url
                    Media = Instance.media_new(playurl)
                    Media.get_mrl()
                    player.set_media(Media)
                    player.play()
                except:
                    talk("Im sorry,I have to play this song on browser")
                    pywhatkit.playonyt(name)
            

            #gogoanime
            elif "stream" in command or "gogoanime" in command:
                try:
                    command= command[(command.index("stream")+len("stream"))+1:]
                    anime_search = anime.get_search_results(query=command)
                    for title in anime_search:
                        title=title.get('animeid')
                        break
                    talk("which episode of "+command+" you want to play senpai?")
                    reply=continue_command()
                    anime_link = anime.get_episodes_link(animeid=title, episode_num=int(reply))
                    clarity_list=[]
                    for x in anime_link:
                        clarity_list.append(x)
                    gogourl=""
                    for x in anime_link["(HDP-mp4)"]:
                        gogourl=gogourl+x
                    talk("Playing episode "+reply+"of"+command)
                    Media = Instance.media_new(gogourl)
                    Media.get_mrl()
                    player.set_media(Media)
                    player.play()
                except:
                    talk("Sorry Senpai,Coudnt find the episode!")
    except:
        pass    
while(True):
    run_alexa()















