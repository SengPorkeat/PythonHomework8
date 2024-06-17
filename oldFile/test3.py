import os
os.system("cls")
khmer_score = float(input("Enter your khmer score: "))
english_score = float(input("Enter your english score: "))
math_score = float(input("Enter your math score: "))

total_score = khmer_score + english_score + math_score
average_score = total_score / 3

print(f"Average: {average_score:.2f}")

if(average_score >= 90):
    print("You get A")
elif(average_score >= 80):
    print("You get B")
elif(average_score >= 70):
    print("You get C")
elif(average_score >= 60):
    print("You get D")
elif(average_score >= 50):
    print("You get E")
else:
    print("You get F")