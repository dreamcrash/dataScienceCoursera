import sys
import json
from pprint import pprint
from collections import Counter

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def readScores(fileName):
    afinnfile = open(fileName)
    scores = {} # initialize an empty dictionary
    
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    
    return scores

def readTweet(fileName):
    data = []
    tweets = []

    with open(fileName) as f:
         for line in f:
             data.append(json.loads(line))
 
    for index in range(len(data)):
        if 'entities' in data[index].keys() and 'hashtags' in data[index]['entities']:
           if data[index]['entities']['hashtags'] != []:
              for hashtag in data[index]['entities']['hashtags']:
                  tweets.append(hashtag['text'])
    return tweets

def giveScore(tweets):
    score = Counter(tweets).most_common(10)

    for k, v in score:
        print k, float(v)

def main():
    tweets = []
    tweet_file = open(sys.argv[1])
    tweets = readTweet(sys.argv[1])
 #   print tweets
    giveScore(tweets)

if __name__ == '__main__':
    main()
