from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']






j=0
for i in range(5):
    color(colors[j])       
    begin_fill()
    for i in range(2):
        left(90)
        forward(80)
        left(90)
        forward(50)

    end_fill()

    forward(50)
    
    j+=1
mainloop()