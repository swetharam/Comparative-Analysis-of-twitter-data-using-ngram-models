import nltk
# import getinput
import string
import re
#things to do in this program: 1) generate tokens new line is a new tweet hence one token at a time, give it to remove stopwords
#just remove the hashtag , compare with the two dictionaries and save the output in a new file maybe?

edited_words=[]

def normalize(sentence):
    tokens = nltk.word_tokenize(sentence)
    removestuff(tokens)

def removestuff(tokens):
        for token in tokens:
            # edited_words.append(token.replace(':','').replace('#','').replace('[^a-zA-Z]+','').replace('"',"").replace('.','').replace('@',''))
            pattern = re.compile('\W')
            edited_words.append(re.sub(pattern, '', token))

for i in range(1,6):
    f = open("input" + str(i)+".txt", "r", encoding="utf-8")
    lines = f.readlines()
    for line in lines:
        normalize(line)
print(edited_words)


