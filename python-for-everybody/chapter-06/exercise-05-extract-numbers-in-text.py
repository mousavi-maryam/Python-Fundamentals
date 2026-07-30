"""
Chapter 6 - Exercise 5

Objective:
Extract a numeric value from a string using the `find()` method and string slicing, 
then convert the extracted substring to a floating-point number.

My Solution:
Stored the input string in a variable and used the `find()` method to locate the position of the colon (`:`). 
Applied string slicing to extract the numeric portion of the string, converted it to a floating-point number using `float()`, 
and displayed the result.
"""

text='X-DSPAM-Confidence:0.8475'
colon_pos=text.find(':')
number=float(text[colon_pos+1:])
print (number)

