from functions import * # import all functions from the module

due_date = input("What is the product's expiration date?\n(Suggested format: dd/mm/yy\nExample: 22.03.2024)\n")

if len(due_date) == 10:
    print(verify_due(due_date))
else:
    print("Error, invalid input!")