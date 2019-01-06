print("Answer the following algebra problem: ")
print("If x = 8, then what's the value of 4(x+3) ?")

result = [35, 36, 40, 44]
for index, i in enumerate(result):
    print(index+1, i, sep=". ")

choice = input("Your answer here")
loop = True 
while loop:
    loop = False
    if int(choice) == 44:
        print("Bingo")
    else:
        print(":(")
        print("Try again")
        choice = input("Your answer here")
        loop = True