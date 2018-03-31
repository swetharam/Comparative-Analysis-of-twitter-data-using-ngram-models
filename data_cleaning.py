import nltk
# import getinput
import string
import re
import nltk
from nltk.corpus import stopwords
#things to do in this program: 1) generate tokens new line is a new tweet hence one token at a time, give it to remove stopwords
#just remove the hashtag , compare with the two dictionaries and save the output in a new file maybe?
abbr = open("abbreviations_dictionary.txt","r", encoding="utf-8")
abbrl=abbr.readlines()
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
        # abbreviation(edited_words)


# def abbreviation(words):
#     for word in words:

for i in range(1,6):
    f = open("input" + str(i)+".txt", "r", encoding="utf-8")
    lines = f.readlines()
    for line in lines:
        normalize(line)

print(edited_words)


