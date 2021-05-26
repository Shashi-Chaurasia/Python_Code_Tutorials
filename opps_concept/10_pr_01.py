class Programmer:
    company = "Microsoft"

    def __init__(self , id , name , salary , designation):
        self.id = id
        self.name = name
        self.salary = salary
        self.designation = designation

    def getInformation(self):
        print(f"{self.id} employee  {self.name} get salary from {self.company} is {self.salary} from branch{self.designation} ")

information = Programmer(6277 , "Shashi" , 69988 , "AWS developer")
information.getInformation()
        
  

        