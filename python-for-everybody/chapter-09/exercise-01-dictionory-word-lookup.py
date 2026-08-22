"""
Chapter 9 - Exercise 1

Objective:
Read the words from a text file and store them as keys in a dictionary. Then use the in operator to check
 whether a given word exists in the dictionary.

My Solution:
Opened a user-specified file, processed each line into individual words, and stored the words as dictionary keys. 
Converted words to lowercase to make the lookup case-insensitive. Added an interactive section that allows the user to 
check whether a word exists in the dictionary.
"""
fname=input('please enter the file name: ')
try:
    fhand=open(fname)

except FileNotFoundError:
    print('The file does not exist')   
    exit()
dictionary=dict()
for line in fhand:
    line=line.strip()
    line=line.lower()
    words=line.split()
    for word in words:
        dictionary[word]=True
while True: 
    word_to_check=(input('please enter a word to check:')).lower()
    if word_to_check=='':
        break
    if word_to_check in dictionary:
        print ('it is in the dictionary')
    else:
        print('it is not in the dicyionary')

