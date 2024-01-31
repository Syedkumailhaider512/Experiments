import pandas as pd
import webbrowser
import wikipedia
import nltk as np
from nltk import word_tokenize, tokenize, stem
from nltk.stem import PorterStemmer , lancaster , WordNetLemmatizer
from nltk.corpus import stopwords
import requests
from bs4 import BeautifulSoup
import transformers
import spacy
import pytextrank
from transformers import PegasusForConditionalGeneration
from transformers import PegasusTokenizer
from transformers import pipeline



query = input("What are you thinking about: ")

nlp = spacy.load("en_core_web_lg")
nlp.add_pipe("textrank")


doc = nlp(query)

phrases = [ (phrase.chunks[0]) for phrase in doc._.phrases ]
tokenize =[]

for w in phrases:
    tokenize.append(str(w))

print(phrases)


'''
tokenize = tokenize.word_tokenize(query)
print(type(tokenize))
print(tokenize)


stemmer = PorterStemmer()
for w in tokenize:
    print(w, " : ", stemmer.stem(w))

lemma = WordNetLemmatizer()

#for w in lemma:
#   print(w, " : ", lemma.lemmatize(w))
'''

stop_words = set(stopwords.words('english'))
filtered_sentence = [w for w in tokenize if not w in stop_words]
filtered_sentence = []

for w in tokenize:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)


google_scholar = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q="
#get_links = requests.get(google_scholar + query)
#print(get_links)

wiki = []

print("Wait, I have to search about it...")
for w in filtered_sentence:
    try:
        w = w.replace('-',' ')
        title = wikipedia.page(w).title
        print("\nI have Something for you about " + w)
        #print(w, " : ", wikipedia.summary(w, sentences=500))
        text_file = open("D:/Programming/Python/Artificial Intellligence/Deep Learning/Neural Network/Reality Neural Network/Data/" +title + ".txt","w")
        text_file.write(wikipedia.summary(w, sentences=500))
        text_file.close()
        #print(w, " : ", webbrowser.open(google_scholar + w))
        print("Data about " + w + " is stored.")

    except Exception as e:
        print("No, I don't know "+ w +". Let's figure out some thing else!")
        #print(w, " : ", "None")


