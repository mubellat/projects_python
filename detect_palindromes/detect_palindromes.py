import math

def is_palindrome(word):
    print(word)
    j = len(word) - 1 # captures the last index of the word
    result = 0
    for i in range(len(word)): # loop to iterate through the word
        if word[i] == word[j]: # compares letter of first index with letter of last index
            result += 1
        if i >= j: # internship to skip the verification because it is already in the middle of the word
            break
        j -= 1

    if result == math.ceil(len(word)/2):
        return True
    else:
        return False
    
def is_palindrome_recursive(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome_recursive(word[1:-1]) # simulation of a loop
    
words = ["racecar", "civic", "refer", "level", "word", "house"]

for word in words:
    print(word)
    print(is_palindrome_recursive(word))
    print("\n") 