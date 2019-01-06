salary = {
    "Huy": 25,
    "Quan": 25,
    "Duc": 30
}

hour = {
    "Huy": 30,
    "Quan": 20,
    "Duc": 40
}

for k in salary.keys():
    print(k)
    print("Salary per Hour: ", salary[k])
    print("Hour: ", hour[k])
    total = 0
    x = salary[k] * hour[k]
    print("Weekly wage", x)

total += x

print("Total salary", total)

