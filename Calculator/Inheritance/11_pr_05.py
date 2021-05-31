class Vector:
    def __init__(self , vec):
        self.vec= vec

    def __str__(self) -> str:
        str = ""
        index = 0
        for i in self.vec:
            str += f"{i}a{index} + "
            index +=1

        return str[:-2]

    def __add__(self , vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])
        return Vector(newlist)

    def __mul__(self , vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

v1 = Vector([2 ,3 , 4])
v2 = Vector([3 ,4 , 6])
print(v1 + v2)
print(v1 * v2)





        






