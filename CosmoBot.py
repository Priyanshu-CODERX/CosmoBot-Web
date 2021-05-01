#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import numpy as np
import random 
import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pyttsx3


# In[2]:


# Initializing Speaking Module
engine = pyttsx3.init()
speaker = engine.getProperty('voice')
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0') # Setting voice property
def speak(speech):
	engine.say(speech)
	engine.runAndWait()
# In[4]:


# nltk.download('punkt')
# nltk.download('wordnet')


# In[4]:


# Opening and Reading the file
filepath='./static/universe.txt'
corpus=open(filepath,'r',errors = 'ignore')
data=corpus.read()
# print (data)


# ## Text Normalization

# In[5]:


# Converting text to Lowercase
data = data.lower()
data


# In[6]:


# Segmenting Sentence

sentence = nltk.sent_tokenize(data)
sentence


# In[7]:


# print(*sentence, sep="\n")


# In[8]:


# Tokenizing Words
words = nltk.word_tokenize(data)
words


# In[9]:


# print(len(sentence), len(words))


# In[10]:


lem = nltk.stem.WordNetLemmatizer()
def LemmatizeTokens(tokens):
    return [lem.lemmatize(token) for token in tokens]


# In[11]:


removePunctuations = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemmatizeTokens(nltk.word_tokenize(text.lower().translate(removePunctuations)))


# In[12]:


# Removing Stop words
sw = nltk.corpus.stopwords.words('english')
sw


# In[13]:


greetings = ["hello", "hi", "greetings", "sup", "what's up","hey", "hey there" , 'konnichiwa', 'namaste', "hela"]
responses = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me", 'satsriyakala']


# In[14]:


def Greet(sentence):
    for word in sentence.split(): # Looks at each word in your sentence
        if word.lower() in greetings: 
            return random.choice(responses)


# In[15]:


def userResponse(res):
    
    botRes = ''
    sentence.append(res)
    tfidfVector = TfidfVectorizer(tokenizer = LemNormalize, stop_words = 'english')
    tfidf = tfidfVector.fit_transform(sentence)
    values = cosine_similarity(tfidf[-1], tfidf)
    idx = values.argsort()[0][-2]
    flat = values.flatten()
    flat.sort()
    reqTfidf = flat[-2]
    
    if(reqTfidf==0):
        botRes = botRes + "Sorry! I can't understand you"
        return botRes
    else:
        botRes = botRes + sentence[idx]
#         speak(botRes)
        return botRes


# In[16]:


# CLI Version

# flag=True
# while(flag==True):
#     user_response = input()
#     user_response=user_response.lower()
#     if(user_response!='bye'):
#         if(user_response=='thanks' or user_response=='thank you' ):
#             flag=False
#             print("Cosmo Bot: You are welcome..")
#         else:
#             if(Greet(user_response)!=None):
#                 print("Cosmo Bot: "+Greet(user_response))
#             else:
#                 print("Cosmo Bot: ",end="")
#                 print(userResponse(user_response))
#                 sentence.remove(user_response)
#     else:
#         flag=False
#         print("Cosmo Bot: Bye! take care..")


# In[17]:


def bot(res):
    user_response = res.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            # speak("You are welcome..")
            return ("You are welcome..")
        else:
            if(Greet(user_response)!=None):
                g = Greet(user_response)
                # speak(g)
                return g
                
            else:
                usr = userResponse(user_response)
#                 print("ROBO: ",end="")
                # speak(usr)
                sentence.remove(user_response)
                return usr
