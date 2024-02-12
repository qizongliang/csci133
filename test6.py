# Use urllib.request to download CPI data from https://raw.githubusercontent.com/compsci-mmakki11/CSCI133/main/cpiai.txt

import urllib.request
url = 'https://raw.githubusercontent.com/compsci-mmakki11/CSCI133/main/cpiai.txt'
book = urllib.request.urlopen(url)
lines = book.readlines()
book.close()

def cleanArr(arr):
    cleaned = []
    for item in arr:
        if(item != ''):
            cleaned.append(item)
    return cleaned

index = 0

data =[]
for line in lines:
    line = line.decode()[:-2]
    if '.' in line:
        if( index >= 18):
            data.append(cleanArr(line.split(' ')))
    index += 1
# Provide a user interface to look up the CPI values for any year. The program should
# read a year number from the keyboard and print out the list of CPI values for
# that year. After that, it should print out the average CPI for that year
# (by computing the average of the reported list).

def average(arr):
    total = 0
    for number in arr:
        total += float(number)
    return total / len(arr)

while True:
    query = input('Enter query:')
    query = query.split(" ")
    curr = []
    display = []
    for item in data:
        if(item[0] == query[0]):
            curr = item[1:13:1]
    if(len(query) == 1):
        print(curr, average(curr))
    else:
        query.pop(0)
        for month in query:
            display.append(curr[int(month)-1])
        print(display, average(display))
        query = []


# Enhance the program by allowing the user to specify the list of months they
# want to see. A valid query may in addition to the year number contain a list
# of mointh numbers separated by spaces. For example, 1950 1 3 5 7 request the data
# for January, March, May, and July of 1950. If the months are not specified,
# report full year. The average should be computed only for the reported months.
