#find the total number of words
totalWords = 0
totalLines = 0
mostWords = 0
mostWordsLine = ''

with open('alice.txt') as book:
    for line in book:
        words = len(line.split())
        totalWords = words + totalWords
        totalLines += 1
        if (mostWords<words):
            mostWords = words
            mostWordsLine = line
print('Total number of words: ',totalWords)

# Find average number of words in a line (total number of words/ total number of lines)
print('Average number of words in a line: ',(totalWords/totalLines))

# The line with the most words and the number of words in that line
print('Longest line has ',mostWords, ' words:',mostWordsLine)

# The total number of lines in your pyhton source code
programLine = 0
with open('test2.py') as program:
    for line in program:
        programLine += 1
print('Total number of lines in Python source code:',programLine)
# Provide an interface that allows the user enter a word to look up
# how many lines contain that word and to see up to the first ten such
# lines, if no lines contain that word, then your program must output Not found

keyword = input("Enter word:")
countLines = 0
lineContain = False
with open('alice.txt') as book:
    for line in book:
        for word in line.split():
            if(keyword in word ):
                lineContain = True
        if lineContain:
            if(countLines < 9):
                print(line)
            countLines+=1
            lineContain = False
if(countLines ==0):
    print("Not found")
else:
    print(countLines, ' lines contain ', keyword)
        
