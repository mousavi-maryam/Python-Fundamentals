fname=input('please enter your file name:')
if fname=="na na boo boo":
    print("you have been punk'd")
    exit()
try:
    fhand=open(fname)
except FileNotFoundError:
    print('file can not be opend:',fname)
    exit()
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1
print('There were',count,'subject lines in', fname)