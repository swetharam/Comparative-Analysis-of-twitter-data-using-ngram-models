import tweepy
consumer_key= '*******************'
consumer_secret='*******************'

access_token='*******************'
access_token_secret='*******************'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api=tweepy.API(auth)
# f=open("input1","w",encoding="utf-8")
i=1;
hashtags=['data',"datascience","animalrescue","peace","marchforourlives"]
for tag in hashtags:
        f = open("input" + str(i), "w", encoding="utf-8")
        for tweet in tweepy.Cursor(api.search,q='#'+tag).items(50):
            f.write(str(tweet.text))
            print(tweet.text)
        i+=1
print("Input done for all hashtags ")