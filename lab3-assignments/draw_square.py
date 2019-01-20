from turtle import *

def square(l,c):
    color(c)
    for j in range (4):
        begin_fill()
        left(90)
        forward(l)
        end_fill()

    
    return[c,l]

# square(100, 'red')

for i in range(30):
    square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()