class C2D:
    def __init__(self ,i , j ) -> None:
        self.icap = i
        self.jcap = j

    def __str__(self) -> str:
        return f"{self.icap}i + {self.jcap}j"
    
class C3D(C2D):
    def __init__(self, i, j , k)  -> None:
        super().__init__(i, j)
        self.kcap = k
        
    def __str__(self) -> str:
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v1 = C2D(1 , 2)
v2 = C3D(2,5,7)
print(v1)
print(v2)
    