import random # library to generate random number

start = input("Hello, shall we start the guessing game? (Y/N)\n")
start = start.upper()
if start == "N":
    quit()

while start != "Y" and start != "N":
    start = input("Invalid option, please try again.\nLet's go? (Y/N)\n")
    start = start.upper()

choice_number = input("Choose the maximum number of numbers in the game (minimum: 5): ")

while not choice_number.isdigit() or int(choice_number) < 5: # # check if the variable is a number or a string
    if not choice_number.isdigit():
        choice_number = input("Invalid! Numbers only, try again: ")
    else:
        choice_number = input("Invalid number, minimum is 5. Try again: ")

choice_number = int(choice_number) # string to number conversion

random_number = random.randint(0, choice_number) # function that generates a random number

attempts = 0

while True:
    answer_user = input("Guess the number: ")
    attempts += 1

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Invalid! Numbers only.  ")
        continue # displays the error message and runs the loop again

    if answer_user == random_number: 
        print("\nCongratulations, you got it right!")
        break # if the user gets the number right, the loop ends
    elif answer_user > random_number:
        print("Failed! Try again:\n(Tip: The number you entered is greater than the correct number)")
    else:
        print("Failed! Try again:\n(Tip: The number you entered is smaller than the correct number)") 

print(f"Number of attempts: {attempts}")