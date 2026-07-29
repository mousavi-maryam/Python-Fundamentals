fname=input("Please enter a file name: ")
try:
    fhand=open(fname)
except FileNotFoundError:
    print('File cannot be opened:',fname)
    exit()

total=0
count=0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        result=float(line.split(':')[1])
        total+=result
        count+=1
if count>0:
    average=total/count
    print(average)
else:
    print("X-DSPAM-Confidence: not found")
