import random
import string # module of the language itself, used to generate lists with string types

def password_generator(len_pass): # parameter is the length of the password characters
    letters_options = string.ascii_letters # generates a list with all the letters of the alphabet (upper and lower case)
    number_options = string.digits # generates all numbers from 0 to 9
    punctuations_options = string.punctuation # # generates all symbols and punctuation marks
    options = letters_options + number_options + punctuations_options # combines all these characters into a single variable

    password_user = ""

    for i in range(0, len_pass):
        digit = random.choice(options) # randomly choose an item from some sequence
        password_user += digit # add the random digit to the variable

    return password_user

while True:
    choice_user = input("How many digits do you want the password to be? (minimum 5 digits) ").strip() # remove empty spaces

    if not choice_user.isdigit(): # check if it has only digits
        print("\nEnter only valid positive whole numbers! Try again.")
        continue # return loop

    choice_user = int(choice_user)

    if choice_user < 5: # checks whether it meets the minimum size requirement
        print("\nMinimum is 5 digits. Try again.")
        continue # return loop

    break # if it passes the checks, the loop ends

print(f"Your password: {password_generator(choice_user)}") # print the generated password