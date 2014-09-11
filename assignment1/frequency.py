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

def giveFreq(tweets):
    freq = {}
    total = 0
    for tweet in tweets:
        for word in tweet.split():
            if word in freq:
               freq[word] += 1
            else:
               freq[word] = 0
            total += 1

    for k in freq:
        print k , float(freq[k])/float(total) 

def main():
    tweets = []
    tweets = readTweet(sys.argv[1])
    giveFreq(tweets)

if __name__ == '__main__':
    main()
