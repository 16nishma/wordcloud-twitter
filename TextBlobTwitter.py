import json
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# am opening tweets_small.json and assigning to a variable called tweetFile
tweetFile = open("tweets_small.json", "r")

# load json from our tweet file
tweetList = json.load(tweetFile)

#close our file because we're done with it
tweetFile.close()

# list of words to filter out
wordsToFilterOut = ["but", "the", "and", "their", "out", "in", "thing", "how", "got", "from", "they", "s", "we", "will", "has", "you", "a", "us", "this", "an", "are", "https", "by", "as", "for", "it", "that", "your", "is", "at", "not", "of", "could", "to", "his", "her", "there", "on", "with", "when", "where", "who", "why", "so", "if"]

# combine all tweets into one giant string
combinedTweetsString = " "
for tweet in tweetList:
    tweetText = tweet["text"]
    combinedTweetsString = combinedTweetsString + tweetText


print (combinedTweetsString)
tweetTextBlob = TextBlob(combinedTweetsString)
filteredOutWordDictionary = dict() # filteredOutWordDictionary = {}

for word in tweetTextBlob.words:
    lowercased_word = word.lower()

    if len(lowercased_word) <= 3:
        continue

    if not lowercased_word.isalpha():
        continue

    #ignore words if it's in our filter list
    if lowercased_word in wordsToFilterOut:
        continue

    filteredOutWordDictionary[lowercased_word] = tweetTextBlob.word_counts[lowercased_word]

print(filteredOutWordDictionary)

#create a word cloud from our words and the frequency with which they appear
wordcloud = WordCloud().generate_from_frequencies(filteredOutWordDictionary)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

""" # make a list to hold our sentiments (feelings refelcted in tweets)
polarity_list = []

# make a list to hold subjectivity
subjectivity_list = []

# get the first tweet from the list of tweets, tweetList
#print(tweetList[0])

# make a loop
# go through every tweet in our tweet list, get the text of the tweet, and then make a TextBlob
# get the polarity score from the TextBlob and append (i.e. add) to the polarity list
for tweet in tweetList:
    tweetblob = TextBlob(tweet["text"])
    polarity_list.append(tweetblob.polarity)
    subjectivity_list.append(tweetblob.subjectivity)


print("\n Here are our polarities: \n", polarity_list)
print("\n Here are our subjectivities: \n", subjectivity_list)

# get average polarity
# get the number of scores in the list
number_of_polarity_scores = len(polarity_list)
# start with a sum of 0.0
sum_of_polarity_scores = 0
# loop through list, and keep adding scores to sum_of_polarity_scores
for polarity_score in polarity_list:
    sum_of_polarity_scores = sum_of_polarity_scores + polarity_score
# divide the sum of polarity scores by the number of scores to get the 'average_polarity_score'
average_polarity_score = sum_of_polarity_scores / number_of_polarity_scores
print("\n Our average polarity score is equal to ", average_polarity_score)


# get average subjectivity
number_of_subjectivity_scores = len(subjectivity_list)
sum_of_subjectivity_scores = 0
for subjectivity_score in subjectivity_list:
    sum_of_subjectivity_scores = sum_of_subjectivity_scores + subjectivity_score
average_subjectivity_score = sum_of_subjectivity_scores / number_of_subjectivity_scores
print("\n Our average subjectivity score is equal to ", average_subjectivity_score) """
