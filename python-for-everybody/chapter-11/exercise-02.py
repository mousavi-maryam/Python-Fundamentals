import re

fname=input('Please enter a file name: ')

count = 0
total=0

try:
    fhand=open(fname)
except FileNotFoundError:
    print(fname,'does not exist')

for line in fhand:
    number=re.findall('^New Revision: ([0-9]+)', line)
    if number:
        count += 1
        total += int(number[0])

print(int(total / count))

