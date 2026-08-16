"""
Chapter 8 - Exercise 4

Objective:
Read a text file, find all unique words, and print them in alphabetical order.

My Solution:
Opened the user-specified file, split each line into words, and added only new words to a list. 
Sorted and printed the final list of unique words. Also added error handling for a missing file.
"""

fname=input("Please enter a file name: ")

words_list=[]

try:
    fhand=open(fname)
    for line in fhand:
        words=line.split()
        for word in words:
            if word in words_list: continue
            words_list.append(word)
    print(sorted(words_list))

    
except FileNotFoundError:
    print("file does not exist")
    exit()
