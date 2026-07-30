"""
Chapter 6 - Exercise 3

Objective:
Create a function that counts how many times a specified letter appears in a given string. 
Generalize the original program by allowing both the string and the target letter to be passed as function arguments.

My Solution:
Defined a `lettercount()` function that accepts a word and a target letter as parameters. 
Used a `for` loop to iterate through each character in the word and a counter variable 
to track the number of matches. Returned the final count and displayed the result using 
user-provided input.
"""

def lettercount(word,desired_letter):
    count=0
    for letter in word:
        if letter==desired_letter:
            count+=1
    return count

word=input("Please enter a word: ")
desired_letter=input("Please enter a letter: ")
print(lettercount(word,desired_letter))
