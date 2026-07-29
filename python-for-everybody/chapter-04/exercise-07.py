def computegrade(score):
    try:
        score=float(score)
        if not 0<=score<=1:
            return "Bad score"
        
        if score>=0.9:
            return "A"
        elif score>=0.8:
            return "B"
        elif score>=0.7:
            return "C"
        elif score>=0.6:
            return "D"
        else:
            return "F"   
            
    except ValueError:
        return "Bad score"

score=input('please enter your score: ')
print(computegrade(score))