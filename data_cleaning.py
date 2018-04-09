import nltk
# import getinput
import string
import sys
import pandas
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
#
alist=[]
with open('engdict.txt') as f:
    alist = [line.rstrip() for line in f]

abbrlist=[]
with open('abbreviations_dictionary.txt') as f:
    abbrlist = [line.rstrip() for line in f]

slanglist=[]
with open('slang_dictionary.txt') as f:
    slanglist = [line.rstrip() for line in f]

print(slanglist)
# things to do in this program: 1) generate tokens new line is a new tweet hence one token at a time, give it to remove stopwords
# just remove the hashtag , compare with the two dictionaries and save the output in a new file maybe?
edited_words=[]
def is_alpha(word):
    try:
        return word.encode('ascii').isalpha()
    except:
        return False

def normalize(sentence):
    tokens = nltk.word_tokenize(sentence)
    removestuff(tokens)

def removestuff(tokens):
        for token in tokens:
            if re.search('[a-zA-Z0_9]',token):
                if token.isalnum():
                    if token.isnumeric():
                        continue
                    else:
                        if token in ["RT" ,"https" , "http"]:
                            continue
                        else:
                            if token in stopwords.words('english'):
                                continue
                            else:
                                edited_words.append(token)


def abbrcheck(word):
    for i in abbrlist:
        if re.match(r'\b' + word + r'\b', i):
            k=i.split(' ', 1)[1]
            temp=word.replace(word,k)
            print(temp)
            return temp


def checkdict(edited_words):
    new_list=[]
    for word in edited_words:
        if word not in alist:
            temp=abbrcheck(word)
            print(temp)
            if temp==None:
                new_list.append(word)
            else:
                new_list.append(temp)
        else:
            new_list.append(word)
    return new_list


def checkslang(edited_words):
        new_list = []
        for word in edited_words:
            if word not in alist:
                temp = slangcheck(word)
                print(temp)
                if temp == None:
                    new_list.append(word)
                else:
                    new_list.append(temp)
            else:
                new_list.append(word)
        return new_list

def slangcheck(word):
        for i in slanglist:
            if re.match(r'\b' + word + r'\b', i):
                k = i.split(' ', 1)[1]
                temp = word.replace(word, k)
                print(temp)
                return temp


# for i in range(1,6):
#     # f = open("input" + str(i)+".txt", "r", encoding="utf-8")
#     # lines = f.readlines()
#     # for line in lines:
normalize("スペイン RT evr lol brb  4u #datascience this is http:""/.893849  data that I am talking about. I love data man! #love acha pasand hai mujhe data")
edited_words=checkdict(edited_words)
edited_words=checkslang(edited_words)
print(edited_words)



######################################################################
#getting a unigram count of all the words:

unigram_table={}

fp = open("test","r",encoding="utf-8")
words=fp.readlines()
tokens = nltk.word_tokenize(words)

for word in tokens:
    if word in unigram_table:
        unigram_table[word]+=1
    else:
        unigram_table[word]=1
print(unigram_table)

