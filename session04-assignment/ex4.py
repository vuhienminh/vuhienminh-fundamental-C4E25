print("Answer the following algebra problem: ")
print("If x = 8, then what's the value of 4(x+3) ?")

correct = 0

result = [35, 36, 40, 44]
for index, i in enumerate(result):
    print(index+1, i, sep=". ")

choice = input("Your answer here")

if int(choice) == 44:
    print("Bingo")
    correct += 1
else:
    print(":(")


print("Estimate this answer (exact calculation not needed): \nJack score these marks in his 5 math test, what's the mean")
answer = ['About 55', 'About 65', 'About 75', 'About 85']
for index, j in enumerate(answer):
    print(index+1, j, sep=". ")

ans = input("Your answer here")

if int(ans) == 2:
    print("Bingo")
    correct += 1
else:
    print(":(")

print("You correctly answer ",correct, "out of 2 answers")