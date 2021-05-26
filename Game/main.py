import random
from typing import Tuple

def newGame(comp , you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'g':
        if you == 'w':
            return None
        elif you == 's':
            return False
    elif comp == 'w':
        if you == 'g':
            return None
        elif you == 's':
            return True

print("Computer tern : snake(s) , water(w) , gun(g) ?")
randm = random.randint(1,3)
if randm == 1:
    comp = 's'
elif randm == 2:
    comp = 'w'
elif randm == 3:
    comp = 'g'

you = input("Your Tern : Chose Snack(s) , Water(w) , gun(g) : ")
a = newGame(randm , you)

print(f"Computer choose : {comp}")
print(f"you choose : {you}")

if a==None:
    print("Match Tie !")

elif a == True:
    print("You win!")

elif a == False:
    print("You Lose!")
    

