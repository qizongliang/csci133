# variables
totalNumberOfTweet = 0
longestTweet = ""
longestTweetWordCount = 0

# The total number of tweets

with open('elon-musk.txt') as tweetHistory:
    for line in tweetHistory:
        totalNumberOfTweet +=1
        currLineWordCount = len(line.split())
        if(longestTweetWordCount < currLineWordCount):
            longestTweet = line
            longestTweetWordCount = currLineWordCount
            
print("Number of tweets: ",totalNumberOfTweet)

# The tweet that contains the most words

print("Tweet with max number of words: ",longestTweet)


# clean the string
def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz@'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

username = "@spacex"

concordance = {}
with open('elon-musk.txt') as tweetHistory:
    for line in tweetHistory:
        for word in cleanedup(line).split():
            if '@' in word:
                if word in concordance:
                    concordance[word]+=1
                else:
                    concordance[word]=1

while True:
    username = input("Enter username: ")
    if(username in concordance):
        print('Found on lines:', concordance[username],'times')
    else:
        print("Not mentioned.")
        
