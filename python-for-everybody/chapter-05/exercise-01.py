total=0
count=0
while True:
    number=input("Enter a number (or type 'done' to finish):")
    if number=="done":
        break
    try:
        number=float(number)
        total=total+number
        count=count+1
    except ValueError:
        print("Invalid input. please enter a number or 'done' to finish.")

if count>0:
    average=total/count
else:
    average=0

print(total, count, average)

   