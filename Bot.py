from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib
import pyaudio
import sys
import time

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def talkToMe(audio): #audio is a string
    print(audio) #print what it is saying
    tts = gTTS(text=audio, lang='en') #displays text gotten from audio in english
    tts.save('audio.mp3')# text is saved
    os.system('mpg123 audio.mp3')#executes audio from the command line

#listens to commands
def myCommand():
    r = sr.Recognizer()#r is now an object which will recognize the voice

    with sr.Microphone() as source:
        r.pause_threshold = 0.5#pause between commands
        r.adjust_for_ambient_noise(source, duration = 1)#makes sure that no small sounds interfere
        audio = r.listen(source)#create audio file from audio it hears from microphone

    try:
        command = r.recognize_google(audio)
        talkToMe('You said: '+ command + '\n')

    #loop back to continue to listen to commands

#if we run into a problem, go back and repeat the function
    except sr.UnknownValueError:
        assistant(myCommand())

    return command
#statements that will execute the commands
def assistant(command):

    if 'Google' in command:
        url = 'https://www.google.com'
        webbrowser.get(chrome_path).open(url)

    if 'twitch' in command:
        url = 'http://www.twitch.tv'
        webbrowser.get(chrome_path).open(url)

    if 'off' in command:
        talkToMe('are you sure?')
        choice = myCommand()
        if 'yes' in choice:
            talkToMe('Shutting Down!')
            time.sleep(3)
            exit()
        else:
            assistant(myCommand())



while True:
    talkToMe('I am listening')
    assistant(myCommand())
