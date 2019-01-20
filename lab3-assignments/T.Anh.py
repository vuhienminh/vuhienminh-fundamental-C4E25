from draw_square import square
from turtle import *

for i in range(30):
    square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()