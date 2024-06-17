import os
os.system("cls")
identity_card =  input("Enter your idetity card: ")
age = int(input("Enter your age: "))
if (identity_card.lower() ==  "khmer" or identity_card.lower() == "kh") and age >= 18:
    print("You are allowed to drive!")
else:
    print("You aren't allowed to drive!")
