""" 
Chapter 6 - Exercise 1

Objective:
Write a program that uses a `while` loop to iterate through a string in reverse order, 
starting from the last character and ending with the first. Print each character on a separate line.

My Solution:
Prompted the user to enter a word and used the `len()` function to determine the index of the last character. 
Implemented a `while` loop to iterate backwards through the string by decreasing the index after each iteration, 
printing one character per line until the beginning of the string was reached.
"""

word=input("Please enter a word:  ")
index=len(word)-1
while index>=0:
    print(word[index])
    index -= 1
