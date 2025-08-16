score = 0
valid_options = ["1", "2", "3", "4"]

def ask_question(question, correct_answer, description_answer):
    global score # using global variable
    global valid_options
    answer = input(f"{question}\nYour answer: ")

    while True: # valid option check
        if answer in valid_options:
            break # end loop
        else:
            print("invalid alternative, try again: ")
            answer = input(question)

    if answer == correct_answer:
        print("Correct alternative, you earned 1 point!\nLet's go to the next question.")
        score += 1
    else:
        print(f"Incorrect alternative!\nCorrect answer: {description_answer}\nBetter luck next time!\nLet's go to the next question.") # displays correct answer

print("Welcome to the science quiz!")
answer_user = input("Shall we start? (Y/N)")
answer_user = answer_user.upper() # convert the string to uppercase

while answer_user != "Y" and answer_user != "N":
    answer_user = input("Incorrect value! Try again.\nShall we start? (Y/N)")
    answer_user = answer_user.upper()

print(f"Selected option: {answer_user}")

if answer_user == "N":
    quit() # if you type "N" the program ends

print("Starting...")
print("You need to get at least 7 right to pass!")

questions = [
    ("What is the basic unit of life?\n1 - Atom\n2 - Cell\n3 - Organ\n4 - Tissue", "2", "2 - Cell"),
    ("What is the main component of plant cells that allows photosynthesis?\n1 - Mitochondria\n2 - Chlorophyll\n3 - Nucleus\n4 - Lysosome", "2", "2 - Chlorophyll"),
    ("Which of these organisms performs photosynthesis?\n1 - Bacteria\n2 - Fungi\n3 - Plants\n4 - Animals", "3", "3 - Plants"),
    ("What is DNA?\n1 - A protein\n2 - A type of cell\n3 - A nucleic acid that carries genetic information\n4 - A type of carbohydrate", "3", "3 - A nucleic acid that carries genetic information"),
    ("What is the function of mitochondria in cells?\n1 - Protein production\n2 - Energy production (ATP)\n3 - Nutrient storage\n4 - Cell reproduction", "2", "2 - Energy production (ATP)"),
    ("Who was the scientist who formulated the theory of evolution of species?\n1 - Isaac Newton\n2 - Albert Einstein\n3 - Charles Darwin\n4 - Louis Pasteur", "3", "3 - Charles Darwin"),
    ("What is cellular respiration?\n1 - Process of converting sunlight into energy\n2 - Process of obtaining energy from food\n3 - Cell division process\n4 - Process of chlorophyll production", "2", "2 - Process of obtaining energy from food"),
    ("Which of the following organisms is classified as a mammal?\n1 - Snake\n2 - Frog\n3 - Bat\n4 - Tree", "3", "3 - Bat"),
    ("What is an ecosystem?\n1 - A set of all species on the planet\n2 - A communication system between organisms\n3 - A set of organisms and the environment in which they live\n4 - The body's defense system", "3", "3 - A set of organisms and the environment in which they live"),
    ("What is mitosis?\n1 - Process of gamete production\n2 - Cell division to form two identical daughter cells\n3 - Growth of an organism\n4 - Energy production in cells", "2", "2 - Cell division to form two identical daughter cells")
]

for i in range(len(questions)):
    print(f"==================== Question {i + 1} ====================")
    ask_question(questions[i][0], questions[i][1], questions[i][2]) 

print(f"You total score: {score}")
if score >= 7:
    print("Congratulations you completed the quiz and passed!")
else:
    print("Failed! You got less than 7 questions right, better luck next time.")