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

def load_data(filename):
    pass

def tokenize(word):
    tokens=word.split(" ")
    for token in tokens:
        token=re.sub(r'\[\ |\~|\`|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\-|\_|\+|\=|\||\\|\[|\]|\{|\}|\;|\:|\"|\'|\,|\<|\.|\>|\/|\?]/g','',token)
        token=token.lower()
    return tokens

def train_data():
    pass

def predict():
    pass
