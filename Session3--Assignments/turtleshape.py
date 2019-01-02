
from turtle import *

# pencolor("red")
# shape("turtle")
# speed(0)

# for i in range(3):
#     left(120)
#     forward(100)

# for i in range(4):
#     pencolor("blue")
#     left(90)
#     forward(100)
    


# for i in range(5):
#     pencolor("purple")
#     left(72)
#     forward(100)
    

# for i in range(6):
#     pencolor("yellow")
#     left(60)
#     forward(100)
    

# for i in range(7):
#     pencolor("grey")
#     left(360/7)
#     forward(100)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
b=3
j=0
for i in range(5):
    for a in range(b):
        pencolor(colors[j])
        left(360/b)
        forward(100)
    b+=1
    j+=1
mainloop()