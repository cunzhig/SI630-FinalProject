import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import pandas as pd

f2 = open("20_train","r")  
lines = f2.readlines()#读取全部内容  

labellist=[]
textlist=[]
for i in lines:
    line=i.strip().split('\t')
    labellist.append(line[1])
    textlist.append(line[0])
f2.close()


def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None # for easy if-statement 

def cleantext(text):
    delEStr = string.digits ##删除数字
    identify = str.maketrans('', '',delEStr)  
    text = text.translate(identify) 
    words=[]
    words=nltk.word_tokenize(text)
    words=[w.lower() for w in words if w.isalpha()] ##转成小写 删除奇怪的标点符号

    stop = stopwords.words('english') + list(string.punctuation) ##删除stopword和标点符号
    all_words=[i for i in words if i not in stop and len(i)>1]

    all_words_pos=nltk.pos_tag(all_words)
    wordnet_lemmatizer = WordNetLemmatizer()
    for i in range(0,len(all_words_pos),1):
        wntag=get_wordnet_pos(all_words_pos[i][1])
        if wntag is None:# not supply tag in case of None
            all_words[i]=wordnet_lemmatizer.lemmatize(all_words[i])
        else:
            all_words[i]=wordnet_lemmatizer.lemmatize(all_words[i],pos=wntag)

    str2 = ' '
    finalstring=str2.join(all_words)

    return finalstring


#print(cleantext("it's the perfect day to sit in one of our hand painted chairs #perfect #day #tryanewteatuesda"))

tweetlist=[]
"""
count=10
for tweet in textlist:
    if count>0:
        tweetlist.append(cleantext(tweet))
        count-=1
    else:
        break
"""
count=0
for tweet in textlist:
    count+=1
    print(count)
    tweetlist.append(cleantext(tweet))


columns = ['text','label']
dataframe=pd.DataFrame({'text':tweetlist,'label':labellist})

dataframe.to_csv("train_cleaned.csv",index=False,sep=",",columns=columns)

