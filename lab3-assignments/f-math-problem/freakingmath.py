from random import *
from calc import eval 

def generate_quiz():
    x = randint(1,50)
    y = randint(1,50)
    f = randint(-1, 1)
    op = choice(['+', '-', '*','/'])
    result = eval(x, y, op) + f
    return [x, y, op, result]

def check_answer(x,f, y, op, result, user_choice):
    
    if f == 0 and user_choice == True :
        return True
    elif f == 0 and user_choice == False :
        return False
    elif not f == 0 and user_choice == True:
        return False
    elif not f == 0 and user_choice == False:
        return True
    return [user_choice, True, False]
    
    
