


class Calc:
    def __init__(self , a , b) -> None:
        self.a = a
        self.b = b

    def add(self):
        print(f"addition : {self.a + self.b}")

    def sub(self):
        print(f"subtraction : {self.a - self.b}")

    def mul(self):
        print(f"multiplication : {self.a * self.b}")

    def div(self):
        print(f"division : {self.a / self.b}")

a= int(input("Enter your first number:"))
b= int(input("Enter your second number:"))

result = Calc(a,b)

result.add()
result.sub()
result.mul()
result.div()

    