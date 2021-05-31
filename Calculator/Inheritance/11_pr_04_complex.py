class Complex:
    def __init__(self , r , i) -> None:
        self.real = r
        self.imaginary = i

    def __add__(self , c):
        return Complex(self.real + c.real  , self.imaginary + c.imaginary) 
    

    def __mul__(self ,c):
        mul_real  = (self.real*c.real ) - (self.imaginary * c.imaginary)
        mul_imaginary  = (self.real*c.imaginary ) + (self.imaginary * c.real)
        return Complex(mul_real , mul_imaginary )

    def __str__(self) -> str:
        return (f" {self.real}  + {self.imaginary}i")


c1 = Complex(3,2)
c2 = Complex(1,7)
print(c1+c2)

print(c1 * c2)
