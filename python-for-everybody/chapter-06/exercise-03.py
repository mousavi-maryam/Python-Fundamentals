def lettercount(word,desired_letter):
    count=0
    for letter in word:
        if letter==desired_letter:
            count+=1
    return count

word=input("Please enter a word: ")
desired_letter=input("Please enter a letter: ")
print(lettercount(word,desired_letter))
