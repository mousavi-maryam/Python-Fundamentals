"""
Chapter 10 - Exercise 3

Objective:
Read a text file, count the frequency of each letter from a-z, and print the letters in decreasing order of frequency.

My Solution:
Converted the input to lowercase, counted the letters using a dictionary and .get(), converted the dictionary 
entries into (count, letter) tuples, sorted them in reverse order, and printed the letter frequencies. 
Added file error handling.
"""


import string
fname=input('please enter a file name: ')
try:
    fhand=open(fname)       
except FileNotFoundError:
    print('The file can not be opened')
    exit()

let_count={}

for line in fhand:
    line = line.lower()

    for letter in line:
        if letter in string.ascii_lowercase:
            let_count[letter] = let_count.get(letter, 0) + 1

lst=[]
for key, val in let_count.items():
    lst.append((val, key))

lst.sort(reverse=True)

for count, letter in lst:
    print(letter,count)