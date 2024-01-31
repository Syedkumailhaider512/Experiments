import pandas as pd
import pyttsx3 as pt
import speech_recognition as sr
import wikipedia
import webbrowser
import nltk as np
from nltk import word_tokenize, tokenize, stem
from nltk.stem import PorterStemmer , lancaster , WordNetLemmatizer
from nltk.corpus import stopwords
import jovian
import os
import webbrowser

a = "Artificial Intelligence"
#wik= wikipedia.summary(a, sentences=5)
#print(wik)

#Speech Engine
engine = pt.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

''''
#Query Generation/Input Generation
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 400
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en_in')
        print(f"User: {query}\n")

    except Exception as e:
        print("Say that again please!")
        # speak("Say That Again please")
        return "None"

    return query

query = takeCommand().lower()
'''

query = input("Tell Your Problem: ")

#Tokenization
tokenize = tokenize.word_tokenize(query)
print(tokenize)


stemmer = PorterStemmer()
for w in tokenize:
    print(w, " : ", stemmer.stem(w))

lemma = WordNetLemmatizer()

#for w in lemma:
#   print(w, " : ", lemma.lemmatize(w))

stop_words = set(stopwords.words('english'))

filtered_sentence = [w for w in tokenize if not w.lower() in stop_words]

filtered_sentence = []

for w in tokenize:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)

google_scholar = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q="

wiki = [w for w in filtered_sentence if not w.lower() in wikipedia.summary(w, sentences=5)]
wiki = []

for w in filtered_sentence:
    if w not in filtered_sentence:
        wiki.append(w)

for w in filtered_sentence:
    print(w, " : ", wiki[wikipedia.summary(w, sentences=5)])
    print(w, " : ", webbrowser.open(google_scholar + w))

