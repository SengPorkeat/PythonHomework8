import os

while True:
    print("===========|| Menu ||=========")
    print("1. Create Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. List Product")
    print("5. Exit")
    op = int(input("Please choose your option: "))
    os.system("cls")
    if op == 1:
        print("You selected create product")
    elif op == 2:
        print("You selected update product")
    elif op == 3:
        print("You selected delete product")
    elif op == 4:
        print("You selected list product")
    elif op == 5:
        print("Exit!")
        break
    else:
        print("Invalid input!")

    