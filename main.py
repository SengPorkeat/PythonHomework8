from utility.menu import menu
from utility.util import *

pathCheck= Path("D:\\ISTAD\\Python")

menu()
while True:
    op = int(input("Choose your option: "))
    if op == 1:
        checkDays(pathCheck)
    elif op == 2:
        deleteFile(pathCheck)
    elif op == 3:
        pass
    elif op == 0:
        break
    else:
        print("Invalid Input !")