from turtle import *
def star(x, y, length):
    speed(0)
    penup()
    setpos(x,y)
    pendown()
    for i in range (5):
        right(144)
        forward(length)
    
    return[x,y, length]

star(144, 144, 50)


speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    star(x, y, length)
mainloop()