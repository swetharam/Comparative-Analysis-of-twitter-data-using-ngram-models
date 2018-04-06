import nltk
# import getinput
import string
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
# print(abbrlist)
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
                            # checkdict(token)

def abbrcheck(word):
    for i in abbrlist:
        if re.match(r'\b' + word + r'\b', i):
            print(i)

# def wordInList(word, listOfWords):
#     for i in listOfWords:
#         if re.match(r'\b' + word + r'\b', i):

def checkdict(editedwords):
    for word in edited_words:
        if word not in alist:
            abbrcheck(word)


# for i in range(1,6):
#     # f = open("input" + str(i)+".txt", "r", encoding="utf-8")
#     # lines = f.readlines()
#     # for line in lines:
normalize("RT lol brb #datascience this is http:""/.893849  data that I am talking about. I love data man! #love acha pasand hai mujhe data")
checkdict(edited_words)
# print(edited_words)