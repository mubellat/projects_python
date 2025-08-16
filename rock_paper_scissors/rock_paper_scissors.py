import random

user_points = 0
computer_points = 0
options = ["R", "P", "S"]

while True:
    user_choice = input("Choice:\n[R] Rock\n[P] Paper\n[S] Scissors\n[Q] Quit game\n").upper()

    if user_choice == "Q":
        print("\nEnd of game!")
        break

    while not user_choice in options:
        print("Invalid option, try again: ")
        user_choice = input("Choice:\n[R] Rock\n[P] Paper\n[S] Scissors\n[Q] Quit game\n").upper()

    computer_choice = random.randint(0, 2)

    computer_option = options[computer_choice]

    '''
    R = 0
    P = 1
    S = 2
    '''

    print(f"The computer chose: {computer_option}")

    if user_choice == computer_option:
        print("Draw!")
    elif user_choice == "R" and computer_option == "S":
        print("Win!")
        user_points += 1
    elif user_choice == "S" and computer_option == "P":
        print("Win!")
        user_points += 1
    elif user_choice == "P" and computer_option == "R":
        print("Win!")
        user_points += 1
    else:
        print("Defeat!")
        computer_points += 1

    print("\nNext round:\n")

print(f"Your score: {user_points}")
print(f"Score computer: {computer_points}")

if user_points > computer_points:
    print("Congratulations, you won!")
elif computer_points > user_points:
    print("You lost, better luck next time.")
else:
    print("Draw!")

print("\nGoodbye!")

