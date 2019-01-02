print("My name is Minh and these are my sheeps'sizes")
size = [5, 7, 300, 90, 24, 50,75]
print(size) 
print("Now my biggest sheep has size ",max(size), "let's shear it")

size[size.index(max(size))] = 8
print("After shearing, here is my flock\n",size) 


for i in range(7):
    size[i] = size[i] + 50
print("Now one month has passed, here is my flock\n",size)

# for j in range(4):
#     for i in range(7):
#     size[i] = size[i] + 50
#     print("Now one month has passed, here is my flock\n",size)

month = int(input("Enter number of month: "))
for j in range(month):
    for i in range(7):
        size[i] = size[i] + 50
    print("Month",j+1)
    print("Now here is my flock\n",size)
    size[size.index(max(size))] = 8
    print("After shearing, here is my flock\n",size) 
print("My flock has size total: ",sum(size))
money = sum(size)*2
print("I would get: ",money,"$")
