import math
class Calculator:
    def __init__(self , number):
        self.number = number

    def square(self):
        print((self.number)**2)

    def suareRoot(self):
        print(math.sqrt(self.number))
    
    def cube(self):
        print((self.number)**3)

    

value = Calculator(6)
value.square()
value.suareRoot()
value.cube()
