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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
    return cleantext


timeMentioned = 0
username = "@SPACEX5"

with open('elon-musk.txt') as tweetHistory:
    for line in tweetHistory:
        temp = line.split()
        for word in temp:
            if('@' in word):
                if()
                if (cleanedup(username) == cleanedup(word)):
                    print(cleanedup(username), cleanedup(word))
                    timeMentioned +=1
            
                
print("Mentioned: ", timeMentioned," times.")
while True:
    username = input("Enter username: ")
    if('@' in username):
        with open('elon-musk.txt') as tweetHistory:
            for line in tweetHistory:
                temp = line.split()
            for word in temp:
                if('@' in word):
                    if (cleanedup(username) == cleanedup(word)):
                        timeMentioned += 1
        print("Mentioned: ", timeMentioned," times.")
        
    else:
        print("Not mentioned.")
        
