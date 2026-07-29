numbers=[]
while True:
    number=input("Enter a number (or type 'done' to finish):")
    if number=="done":
        break
    try:
        number=float(number)
        numbers.append(number)
    except ValueError:
        print("Invalid input. please enter a number or 'done' to finish.")

if numbers:
    print("Minimum:", min(numbers))
    print("Maximum:", max(numbers))
else:
    print("No numbers entered.")