fname=input('please enter your file name:\n')
try:
    fhand=open(fname)
except FileNotFoundError:
    print('File cannot be opened:',fname)
    exit()

for line in fhand:
    print(line.rstrip().upper())