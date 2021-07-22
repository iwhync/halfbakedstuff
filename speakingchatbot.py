import speech_recognition as sr
import pyttsx3
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import spacy
from tkinter import *
from chatterbot import *
import random

chatbot = ChatBot("Name")

spacy.load('en_core_web_sm')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
# Train based on the english corpus
trainer.train("chatterbot.corpus.english")
# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")
# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")



engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', 110) # Decrease the Speed Rate x2
engine.setProperty('voice', voices[2].id)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
r = sr.Recognizer()
mic = sr.Microphone()
engine.runAndWait()
a = True
while a == True:
    try:
        with mic as source:
            audio = r.listen(source)
        x = r.recognize_google(audio)
        print(f"you said {x}")
        y = chatbot.get_response(x)
        print(f"chatbot said {y}")
        engine = pyttsx3.init()
        engine.say(y)
        engine.runAndWait()
        a -= 1
        engine.stop()
    except:
        what = random.randint(1,3)
        if what == 1:
            y = "Sorry I didn't understand that."
            engine.say(y)
            engine.runAndWait()
        if what == 2:
            y = "Can you repeat that?"
            engine.say(y)
            engine.runAndWait()
        else:
            y = "I don't know what you mean"
            engine.say(y)
            engine.runAndWait()
