import os,sys,re,csv
import pickle
from collections import Counter, defaultdict
import numpy as np
import scipy
import math
import random
import nltk
from scipy.spatial.distance import cosine
from nltk.corpus import stopwords
from numba import jit
import matplotlib.pyplot as plt

tweets=[]
emojis=[]

def load_data(filename):
    #load date into two list, tweets and emojis
    global tweets
    global emojis
    f = open(filename, "r", encoding="utf8")
    rows =f.read().split("\n")
    for each in rows:
        row=each.split("\t")
        if len(row)==2:
            tweet=row[0]
            tweets.append(tweet)
            emoji=row[1]
            emojis.append(emoji)

def calculate_most_frequent_emoji(emojis):
    print(emojis)
    emoji_dict={}
    for emoji in emojis:
        if emoji not in emoji_dict:
            emoji_dict[emoji]=1
        else:
            emoji_dict[emoji]+=1
    #print（sorted(emoji_dict(), key=lambda d: d[1])）
    #print(emoji_dict)



def train_data():
    pass

def predict():
    pass

load_data("20_train")
calculate_most_frequent_emoji(emojis)
