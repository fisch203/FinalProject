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


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print('This is my final project program.')
print('The objective is to receive the last 500 tweets from our president elect from the twitter API.')
print('The program will then count how many times each word is used (words only used once are not considered)')
print('Then the program will print the results of the search into a text file (results.txt)')
time.sleep(8)


word_count = {}
#This line collects tweets from user 25073877 (realDonaldTrump) and will collect 500
status_list = api.user_timeline(user_id = 25073877, count=500)

#Go through all 500 tweets
for i in status_list:
    tweet_text = i.text

#strip all punctuation from the tweets
    for c in tweet_text:
        if c in string.punctuation:
            tweet_text = tweet_text.replace(c, '')
        if c == "\\":
            tweet_text = tweet_text.replace(c, '')

    good_list = []
    tweet_list = tweet_text.split()

# strip all words that wont print to the text file by sorting good words into "good_list"
    for item in tweet_list:
        if all(ord(char) < 128 for char in item):
            good_list.append(item)

#count usage of each word in the list
    for w in good_list:
        w = w.lower()

#discount the "words" that are links
        if 'http' in w:
            break
        elif ord(w[-1]) >= 128:
            break

#count all of the remaining words
        if w in word_count:
            if len(w) > max_len:
                max_len == len(w)
            word_count[w] += 1
        elif w not in word_count:
            word_count[w] = 1


final_cnt = collections.OrderedDict(sorted(word_count.items(), key=operator.itemgetter(1)))

save_file = open('results.txt','w')
save_file.write('DONALD TRUMPS FAVORITE WORDS\n')

#write all the words and their counts to a text file. discount words that were only used once
for i in reversed(final_cnt):
    if final_cnt[i] > 1:
        save_file.write(i)

# the number of "|"'s denotes the amount of times the word was used
        for z in range(final_cnt[i]):
            save_file.write('|')
        save_file.write('\n')
save_file.close() 