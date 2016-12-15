#Import the necessary methods from tweepy library
import tweepy
import json
import operator
import string
import collections
import time


#Variables that contains the user credentials to access Twitter API 
access_token = "808741181010169856-eu7PcjYCTsUJPhyd2OiZkcnjhZCKJrz"
access_token_secret = "XQiVmrO6nuCJwiFsxVK2258ig4SSwuR4MpkIIqExLqeqC"
consumer_key = "5iwpZKk2DGpcLRT14hO3kuuwJ"
consumer_secret = "JWPi0D4WHHf1ygycGj9MnaGzIFPlT9baULL0wyXidkwVs02Tzz"





#This handles Twitter authetification and the connection to Twitter Streaming API
# l = StdOutListener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# stream = Stream(auth, l)
api = tweepy.API(auth)

word_count = {}
#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
status_list = api.user_timeline(user_id = 25073877, count=500)
for i in status_list:
    tweet_text = i.text
    for c in tweet_text:
        if c in string.punctuation:
            tweet_text = tweet_text.replace(c, '')
        if c == "\\":
            tweet_text = tweet_text.replace(c, '')

    good_list = []
    tweet_list = tweet_text.split()

    for item in tweet_list:
        if all(ord(char) < 128 for char in item):
            good_list.append(item)
    # print (tweet_text)

    for w in good_list:
        w = w.lower()
        if 'http' in w:
            break
        elif ord(w[-1]) >= 128:
            break
        if w in word_count:
            word_count[w] += 1
        elif w not in word_count:
            word_count[w] = 1


final_cnt = collections.OrderedDict(sorted(word_count.items(), key=operator.itemgetter(1)))

save_file = open('results.txt','w')
for i in reversed(final_cnt):
    if final_cnt[i] > 1:
        save_file.write(i)
        for z in range(final_cnt[i]):
            save_file.write('|')
        save_file.write('\n')
save_file.close() 