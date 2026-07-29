string='X-DSPAM-Confidence:0.8475'
colonpos=string.find(':')
number=float(string[colonpos+1:])
print (number)

