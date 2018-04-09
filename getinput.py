import tweepy
import re
import nltk
from nltk.corpus import stopwords
consumer_key= 'Quo2d5FNN6F9LNwqOExTufMxR'
consumer_secret='qKHT8wy8PGrf7NcsONuUtk0RWhnvCrYbNp6NPqFOJbR4ZQldsT'

access_token='914577085347323906-YtVrpvFXrUZHt5v6rTdnl0tr6KY0cjs'
access_token_secret='rZzCmPxP5ZS8FNfXt4MT3QAzuAfFPCOeSmDx44XaaEahs'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# api=tweepy.API(auth)
train=open("train","w",encoding="utf-8")
test=open("test","w",encoding="utf-8")
#experimental section using lists
i=1

###############################################################################################################
alist=[]
with open('engdict.txt') as f:
    alist = [line.rstrip() for line in f]

abbrlist=[]
with open('abbreviations_dictionary.txt') as f:
    abbrlist = [line.rstrip() for line in f]

slanglist=[]
with open('slang_dictionary.txt') as f:
    slanglist = [line.rstrip() for line in f]
########################################################
k=1
hashtags=['data',"datascience","machinelearning","bigdata","analytics","python","deeplearning","datascientists","AI","ML"]
list=[]
listtest=[]
editedtest=[]
editedtrain=[]

########################################################################################################################
#STEP 1: GET THE DATA FROM TWITTER
for tag in hashtags:
    for tweet in tweepy.Cursor(api.search,q='#'+tag).items(50):
                temp = []
                if k<36:
                    list.append(tweet.text)
                    k+=1
                else:
                    temp.append(tweet.text)
                    listtest.append(temp)
                    k+= 1

#Second step in data normalization is removal of stop words, abbreviations being replaced with their full forms and
#slang words being replaced with their original words

def abbrcheck(word):
    for i in abbrlist:
        if re.match(r'\b' + word + r'\b', i):
            k=i.split(' ', 1)[1]
            temp=word.replace(word,k)
            # print(temp)
            return temp


def checkdict(edited_words):
    new_list=[]
    for word in edited_words:
        if word not in alist:
            temp=abbrcheck(word)
            # print(temp)
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
                # print(temp)
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
                return temp


def removestuff(tokens):
    for token in tokens:
        if re.search('[a-zA-Z0_9]', token):
            if token.isalnum():
                if token.isnumeric():
                    continue
                else:
                    if token in ["RT", "https", "http"]:
                        continue
                    else:
                        if token in stopwords.words('english'):
                            continue
                        else:
                            editedtrain.append(token)

def removestufftest(tokens):
    temparr=[]
    for token in tokens:
        if re.search('[a-zA-Z0_9]', token):
            if token.isalnum():
                if token.isnumeric():
                    continue
                else:
                    if token in ["RT", "https", "http"]:
                        continue
                    else:
                        if token in stopwords.words('english'):
                            continue
                        else:
                            temparr.append(token)
    return temparr




#This performs normalization of data, first step here is tokenization.
def normalize(sentence):
    tokens = nltk.word_tokenize(sentence)
    removestuff(tokens)

def normalize1(sentence):
    temparr = []
    tokens = nltk.word_tokenize(sentence)
    removestufftest(tokens)
    temparr=removestufftest(tokens)
    editedtest.append(temparr)

########################################################################################################################
#STEP 2: HERE WE ARE PERFORMING A BUNCH OF DATA CLEANING OPERATIONS
for tweet in list:
    normalize(tweet)

for sentence in listtest:
    senstr=sentence[0]
    normalize1(senstr)

print(editedtest)
#traing data checking the slang and abbr dictionaries
editedtrain=checkdict(editedtrain)
editedtrain=checkslang(editedtrain)

#writing the sentences in a file:

# for words in editedtest:
#     test.write(words+" ")
# for words in editedtrain:
#     train.write(words+" ")

##############################################
#unigram model generation
unigram_count={}
for word in editedtrain:
    if word in unigram_count:
        unigram_count[word]+=1
    else:
        unigram_count[word]=1

print(unigram_count)
totalwords=len(unigram_count.keys())

unigram_prob={}
for word in editedtrain:
    temp=unigram_count[word]/totalwords
    unigram_prob[word]=temp
print(unigram_prob)

##################################################################
unigram_count_test={}
i=0
for list in editedtest:
    temp = {}
    for word in list:
        if word in temp:
            temp[word] += 1
        else:
            temp[word] = 1
    unigram_count_test[i]=temp
    i+=1

unigram_total_test={}
i=0
for list in editedtest:
    temp = {}
    k=0
    for word in list:
       k+=1
    unigram_total_test[i]=k
    i+=1
unigram_prob_test={}
i=0
for list in editedtest:
    temp=1
    for word in list:
        if word in unigram_prob:
            temp=unigram_prob[word]*temp
    unigram_prob_test[i]=temp
    i+=1

print(unigram_prob_test)