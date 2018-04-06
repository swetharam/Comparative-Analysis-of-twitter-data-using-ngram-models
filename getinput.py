import tweepy
import nltk
from nltk.corpus import stopwords
consumer_key= 'Quo2d5FNN6F9LNwqOExTufMxR'
consumer_secret='qKHT8wy8PGrf7NcsONuUtk0RWhnvCrYbNp6NPqFOJbR4ZQldsT'

access_token='914577085347323906-YtVrpvFXrUZHt5v6rTdnl0tr6KY0cjs'
access_token_secret='rZzCmPxP5ZS8FNfXt4MT3QAzuAfFPCOeSmDx44XaaEahs'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api=tweepy.API(auth)
train=open("train","w",encoding="utf-8")
test=open("test","w",encoding="utf-8")
#experimental section using lists
i=1



########################################################
k=1
hashtags=['data',"datascience","machinelearning","bigdata","analytics","python","deeplearning","datascientists","AI","ML"]
list=[]
listtest=[]
editedtest=[]
editedtrain=[]
for tag in hashtags:
    for tweet in tweepy.Cursor(api.search,q='#'+tag).items(50):
                if k<36:
                    # f.write(str(k)+":"+str(tweet.text))
                    list.append(tweet.text)
                    # print(str(k)+":"+tweet.text)
                    k+=1
                else:
                    # f1.write(str(k) + ":" + str(tweet.text))
                    listtest.append(tweet.text)
                    # print(str(k) + ":" + tweet.text)
                    k+= 1


def removestuff(tokens):
        for token in tokens:
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
                            # if key=="set":
                            editedtrain.append(token)
                            # else:
                            #     editedtest.append(token)
                            # print(token)


def normalize(sentence):
    tokens = nltk.word_tokenize(sentence)
    removestuff(tokens)
key="set"
for tweet in list:
    normalize(tweet)

# key="unset"
# for tweet in listtest:
#     normalize(tweet)

# print("train set")
# print(editedtrain)
# print("test set")
# print(editedtest)