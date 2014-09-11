import sys
import json
from pprint import pprint

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
        if 'text' in data[index]:
           tweets.append(data[index]["text"])
    return tweets

def giveScore(scores,tweets):
    score = 0
    for tweet in tweets:
        score = 0
        for word in tweet.split():
            if word in scores:
               score = score + scores[word]
        print score
    


def main():
    scores = []
    tweets = []
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = readScores(sys.argv[1])
    tweets = readTweet(sys.argv[2])
    giveScore(scores,tweets)

if __name__ == '__main__':
    main()
