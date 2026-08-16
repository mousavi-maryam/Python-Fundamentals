
"""
Chapter 8 - Exercise 1

Objective:
Write two functions: chop() to remove the first and last elements of a list and modify the original list,
 and middle() to return a new list containing all but the first and last elements.

My Solution:
Implemented the chop() function using the del statement to modify the original list and the middle()
function using list slicing to return a new list. Collected user input in a list with a while 
loop and demonstrated the behavior of both functions.
"""


def chop(t):
    if len(t)>1:
        del t[0]
        del t[-1]
    return None

def middle(t):
    if len(t)>1:
        return t[1:-1]
    return []
    
lst=[]
while(True):
    inp=input('please enter a character:')
    if inp=='done':
        break
    lst.append(inp)


print(middle(lst))
print(lst)

print(chop(lst))
print(lst)
