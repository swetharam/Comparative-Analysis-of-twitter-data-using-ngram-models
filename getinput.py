import tweepy
import re
import nltk
from nltk.corpus import stopwords
import numpy as np
from nltk.util import ngrams
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
tempfile=open("tempfile","w",encoding="utf-8")
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
hashtags=['data'] #,"datascience","machinelearning","bigdata","analytics","python","deeplearning","datascientists","AI","ML"]
list=[]
listtest=[]
editedtest=[]
editedtrain=[]
editedtestbackup=[]

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
# print(editedtest)
#traing data checking the slang and abbr dictionaries

editedtrain=checkdict(editedtrain)
editedtrain=checkslang(editedtrain)


#important step: making all the edits:
temp1=[]
temp2=[]
for list in editedtest:
    temp1=checkdict(list)
    temp2.append(temp1)
editedtest=temp2

temp1=[]
temp2=[]
for list in editedtest:
    temp1=checkslang(list)
    temp2.append(temp1)
editedtest=temp2

for word in editedtest:
    for item in word:
        editedtestbackup.append(item)

for words in editedtestbackup:
    test.write(str(words+" "))
test.close()
testbackup=open("test","r",encoding="utf-8")
variable=testbackup.readlines()
editedtestbackup=variable[0].split()
print(editedtestbackup)


backupcount={}
for words in editedtestbackup:
    backupcount[words]=1
    if words in editedtrain:
        backupcount[words]+=1
print(backupcount)

####################################################
#writing the sentences in a file:

# for words in editedtest:
#     test.write(words+" ")
for words in editedtrain:
    train.write(words+" ")
train.close()
##############################################
traindata=open("train","r",encoding="utf-8")
trainlines=traindata.readlines()
##############################################
# #unigram model generation
unigram_count={}
for word in editedtrain:
    if word in unigram_count:
        unigram_count[word]+=1
    else:
        unigram_count[word]=1
# print("Unigram count of the words in the train data")
# print(unigram_count)
totalwords=len(unigram_count.keys())

unigram_prob={}
for word in editedtrain:
    temp=unigram_count[word]/totalwords
    unigram_prob[word]=temp
# print("Unigram probabilities of the individual words in the train data")
# print(unigram_prob)

# #################################################################
# # testing the unigram models on the testing data
#
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
# print("Unigram sentence each word's total ")
# print(unigram_count_test)
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

# print("U-test prob"+str(unigram_prob_test))
test_len=len(unigram_prob_test)
temp=0
k=0
for prob in unigram_prob_test:
    temp=temp+unigram_prob_test[k]
    k+=1
avgtest=temp/test_len
print("Average unigram probability")
print(avgtest)

#generation of bigram models:


arr=[]
for sent in editedtest:
    # print(sent)
    s2=[]
    for ngram in ngrams(sent, 2):
        s2.append(' '.join(str(i) for i in ngram))
    arr.append(s2)
print(arr)
specialbigram={}
bigrams1count_test={}
for list in arr:
    for words in list:
        bigrams1count_test[words]=1
        if words in trainlines:
            bigrams1count_test[words]+=1
            specialbigram[words]=bigrams1count_test[words]

print("Bigram word counts")
print(bigrams1count_test)
tempfile.write(str(bigrams1count_test))
i=0
###########
# #getting the total words in each sentence:
test_count=[]
for list in editedtest:
    temp=0
    for word in list:
        temp+=1
    test_count.append(temp)
#imp
print("No of words in each sentence")
print(test_count)

bigramprob=[]
i=0

for list in arr:
    current = 1
    for words in list:
        k=0
        temp=bigrams1count_test[words]
        temp1=words.split()
        abc=""+temp1[0]
        value=backupcount[abc]
        current=(current*temp)/(value*test_count[i])
    bigramprob.append(current)
    i+=1
print(bigramprob)
for prob in bigramprob:
    temp=temp+prob
bigramavg=temp/test_len
print("Average bigram probability")
print(bigramavg)
################################################
#trigram calculations
arr1=[]
for sent in editedtest:
    # print(sent)
    s2=[]
    for ngram in ngrams(sent, 3):
        s2.append(' '.join(str(i) for i in ngram))
    arr1.append(s2)
print(arr1)

trigramcount_test={}
for list in arr1:
    for words in list:
        trigramcount_test[words]=1
        if words in trainlines:
            trigramcount_test[words]+=1

print("Trigram word counts")
print(trigramcount_test)
i=0
specialcount=len(specialbigram)
trigramprob=[]
for list in arr1:
    current = 1
    for words in list:
        k=0
        temp=trigramcount_test[words]
        temp1=words.split()
        abc=str(temp1[0])+" "+str(temp1[1])
        if specialcount>0:
            value=specialbigram[abc]
        else:
            value=1
        current=(current*temp)/(value*test_count[i])
    trigramprob.append(current)
    i+=1
print("Trigram probabilities:")
print(trigramprob)
for prob in trigramprob:
    temp=temp+prob
trigramavg=temp/test_len
print("Average bigram probability")
print(trigramavg)