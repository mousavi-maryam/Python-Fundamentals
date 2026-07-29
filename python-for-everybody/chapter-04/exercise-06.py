def computepay(hours,rate):
    if hours<=40:
        return hours * rate
    else:
        overtime=hours-40
        return ((40 * rate) +( overtime * 1.5 * rate))
    

hours=float(input('please enter number of hours you have worked:\n'))
rate= float(input('please rnter your pay rate:\n'))
pay= computepay(hours,rate)

print ('pay:', pay)