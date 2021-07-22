import pyttsx3
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', 110) # Decrease the Speed Rate x2
engine.setProperty('voice', voices[0].id)

consonant = "bcdfghjklmnprstvwxz"
vowel = "aeiou"
word = []
for _ in range(random.randint(2,14)):
    word.append(consonant[random.randint(0,len(consonant)-1)])
    word.append(vowel[random.randint(0,len(vowel)-1)])
word = "".join(word)
print(word)
engine.say(word)
engine.runAndWait()
