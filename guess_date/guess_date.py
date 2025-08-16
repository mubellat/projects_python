import json # import the file .json
import random

open_json = open("dates.json", encoding="utf8") # allows opening the specified .json file, we also specify the decoding pattern
 
dates = json.load(open_json) # opening file
choice_computer = random.choice(list(dates.keys())) # converting to lists and listing keys

print("Hello, welcome!")
print("===============")

number_choices = 5
win = False

while number_choices > 0 and win is not True:
    print(f"Tip: {dates[choice_computer]}")
    answer_user = input("Data(DD/MM/AAAA): ")
    print("==================== \n")

    if len(answer_user) != 8: # verification
        print("Invalid, the answer must contain 8 digits.")
        continue

    if answer_user.isdigit(): # verification
        check = []
        pontuation = 0
        for i in range(8):
            if answer_user[i] == choice_computer[i]:
                check.append("✅")
                pontuation += 1
            else:
                check.append("❌")

        print("Response: \n")
        print("|".join(check)) # adds the slash to separate each element of the list
        print(" |".join(answer_user))
        print("====================\n")

        if pontuation == 8:
            win = True
    else:
        print("Invalid, the response must be in date format.")
        continue

    number_choices -= 1

if win == True:
    print("VICTORY!!!")
else:
    print("Defeat, better lucky next time!")
    print(f"Correct answer: {choice_computer}")