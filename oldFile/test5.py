import os
os.system("cls")

# for i in range(11):
#     print(i, end=" ")
#     if(i == 5):
#         break

for i in range(11): 
    if(i % 2 == 0):
        continue
    print(i, end=" ")