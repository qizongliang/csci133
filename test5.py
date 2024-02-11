import os

#Modify function Cleanedup so that it keeps not only letters, but also digits
#0123456789 and symbols @and _

# clean the string
def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz@_0123456789'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext
#print(findMentions("xxx"))

#Write a new function findMentiuons that takes a filename as a parameter and
#reports 3 usernames most frequently mentioned in that file. The function should
#a dictionary of counts for all username mentions (words starting with @). After
#reading through the file and accumulating the counts for all mentioned usernames
#, use the dictionary to create a list
# use sort to sort the list and print out 3 most freuquntly mentioned usernames.

def findMentions(filename):
    topThree = []
    entireArr = []
    concordance = {}
    with open(filename,encoding="utf-8") as tweetHistory:
        for line in tweetHistory:
            for word in cleanedup(line).split():
                if '@' in word:
                    if word in concordance:
                        concordance[word]+=1
                    else:
                        concordance[word]=1
    for word in concordance:
        tempArr = []
        tempArr.append(concordance[word])
        tempArr.append(word)
        entireArr.append(tempArr)
    entireArr.sort()
    for index in range(3):
        topThree.append(entireArr[len(entireArr)-3+index])
    return topThree

#Check each file in the current folder(using os.listdir('.'))
path = '.'
for filename in os.listdir(path):
    temp = filename.split('.')
    if(len(temp)== 2):
        if( temp[1] == 'tweets'):
            print(filename)
            for i in findMentions(filename):
                print("     ",i[1],i[0])
            

