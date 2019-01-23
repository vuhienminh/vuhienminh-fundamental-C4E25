# x = int(input("Please enter x"))
# y = int(input("Please enter y"))
# f = input("Please enter operator")

# result = 0
# from random import randint, choice


# x = randint(1,50)
# y = randint(1,50)
# f = randint(-1, 1)
# op = choice(['+', '-', '*','/'])

def eval(x,y,op):
    result = 0
    if  op == "-":
        result = x - y
    elif op == "+":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y
    return result

# r = eval(4,7,"-")
# print(r)

# print(x, op, y,"=", result)

# print(result)

# def sayHi(n):         #n~ tham so ham(parameters)           #function body
#     print("Hi")
#     print("Hi", n )
#     print("Bye bye")

# sayHi("Quan")
# sayHi("Minh")

# def add(x, y):
#     r = x + y
#     return r

# s = add(3, 4)
# print(s)
