
import tweepy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
# Download required NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
# Authenticate with Twitter API
consumer_key = "LMwvRn4KV2qWwNI7ZhyWLNIhw" 
consumer_secret = "nB324r6e4Rz19LsFJPbBYnCEwWw8VcLatTlAtV05v7K7oQykrP" 
access_token = "2008441416264151040-WQ4bgM1DzpcYKWO5SsTzsFr33gAZ55" 
access_token_secret = "cIIEQkRSIq8rcOyt782yBnwY22tJqCw7TECAaGMPjcWSF" 
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token,access_token_secret)
api = tweepy.API(auth)
#sample tweets
tweets = [ 
    "Learning Python is fun",
    "Coding makes life easier",
    "Practice improves programming",
    "Errors help us learn",
    "Technology changes the world"
]
#analyze tweets
def preprocess(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    return [t for t in tokens if t.isalnum() and t not in stop_words]
text = " ".join(tweets)
counter = Counter(preprocess(text))
#printing top 10 frequency words in tweet content
print("Top 10 Most Frequent Words in Tweets:")
for i, (word, freq) in enumerate(counter.most_common(10), start=1):
    print(f"{i}. {word} - {freq}")
#visualize tweets with frequency analysis
top_words = dict(counter.most_common(10))
#graph representation
plt.figure(figsize=(5, 5))
plt.bar(top_words.keys(), top_words.values(), color='purple')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top {} Most Frequent Words in Tweets'.format(10))
plt.xticks(rotation=45)
plt.show()
