import tweepy
consumer_key= 'Quo2d5FNN6F9LNwqOExTufMxR'
consumer_secret='qKHT8wy8PGrf7NcsONuUtk0RWhnvCrYbNp6NPqFOJbR4ZQldsT'

access_token='914577085347323906-YtVrpvFXrUZHt5v6rTdnl0tr6KY0cjs'
access_token_secret='rZzCmPxP5ZS8FNfXt4MT3QAzuAfFPCOeSmDx44XaaEahs'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api=tweepy.API(auth)
# f=open("input1","w",encoding="utf-8")
i=1
hashtags=['data',"datascience","animalrescue","peace","marchforourlives"]
for tag in hashtags:
        k=1
        f = open("input" + str(i)+".txt", "w", encoding="utf-8")
        for tweet in tweepy.Cursor(api.search,q='#'+tag).items(50):
            f.write(str(k)+":"+str(tweet.text))
            print(str(k)+":"+tweet.text)
            k+=1

        i+=1
print("Input done for all hashtags ")