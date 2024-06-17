import os
os.system("cls")

def pizza(*toppings):
    for allToping in toppings:
        print(f"- {allToping}")

pizzaToppings = input("Insert Toppings: ").split(",")
print("Pizza Toppings 🍕")
for pizzaTopping in pizzaToppings:
    pizza(pizzaTopping)