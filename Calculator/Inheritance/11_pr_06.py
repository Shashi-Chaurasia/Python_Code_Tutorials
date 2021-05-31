class Vector:
    def __init__(self , vec) -> None:
        self.vec = vec
   

    def __str__(self) -> str:
        return(f"{self.vec[0]}i + {self.vec[1]}j + { self.vec[2]}k")

    def __len__(self):
        return(len(self.vec))



v1 = Vector ([2,4,6])
v2 = Vector ([1,3,9])
print(len(v1))
print(v2)