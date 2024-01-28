# Have your program check the word coronavirus
# itself and report what unique letters it contains

alphabets = 'abcdefghijklmnopqrstuvwxyz'
word = 'coronavirus'
for letter in alphabets:
    if letter in word:
        print(word, ' cotains ', letter)

# Generate a series of questions of the form, "Can X treat Y?"
# where X is the following lsit of medications: Remdesivir, Hydroxychloroquine,
# Kaletra, favipiravir
# and Y is the following list of diseases: coronavirus,
# hepatitis, malaria, influenza


medications = ['remdesivir','hydroxychloroquine','kaletra','favipiravir']
diseases = ['coronavirus','hepatitis','malaria','influenza']

for medicine in medications:
    for disease in diseases:
        print('Can ', medicine, ' treat ', disease,'?')

# In this step, your program will search for common letters in some words that
# were uncommon before the coronavirus outbreak. Take each letter in the word
# 'coronavirus' and report whether each letter also exists in each medication
# from the list of medications 

for letter in alphabets:
    if letter in word:
        for medicine in medications:
            if letter in medicine:
                print(letter, ' is in ',word, ' and also in ',medicine)
