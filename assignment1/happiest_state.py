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

def readTweet(fileName,scores):
    data = []
    tweets = {}

    with open(fileName) as f:
         for line in f:
             data.append(json.loads(line))

    for index in range(len(data)):
	if 'text' in data[index] and 'place' in data[index] and data[index]['place'] is not None:
           if 'country_code' in data[index]['place'] and data[index]['place']['country_code'] == 'US':
               state =  data[index]['place']['full_name'].encode('utf8').split(', ')
               pprint (state)
               if state[1] != 'US':
                  if state[1] in tweets:
                     tweets[state[1]] += giveScore(scores,data[index]['text'])
                  else: 
                     tweets[state[1]] = giveScore(scores,data[index]['text'])
              
    return tweets

def theHappiest(tweets):
    if tweets:
       k = max(tweets, key=tweets.get)
       print k[0:2]
     

def giveScore(scores,tweet):
    score = 0
    for word in tweet.split():
        if word in scores:
           score = score + scores[word]
    return score
    


def main():
    scores = []
    tweets = []
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = readScores(sys.argv[1])
    tweets = readTweet(sys.argv[2],scores)
    theHappiest(tweets)
if __name__ == '__main__':
    main()
