import os
os.system("cls")
# Lambda or Anonymous function
# x = lambda a : a + 10
# y = lambda a,b : a * b

# print(x(5))
# print(y(2,10))

# def function_lambda(x):
#     x("Alex")

# function_lambda(lambda x: print(f"This is {x}"))

scoreFunction = [90,40,85,35,20,78,98]

def myFilterFunction(compareFunction,scoreFunction):
    filterScoreFunction = []
    for score in scoreFunction:
        if(compareFunction(score)):
            filterScoreFunction.append(score)
    return filterScoreFunction

print(myFilterFunction(lambda scoreFunction: scoreFunction >= 80,scoreFunction))