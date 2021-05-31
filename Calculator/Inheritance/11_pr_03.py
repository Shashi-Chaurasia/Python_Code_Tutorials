class Emaployee:
    salary = 5000
    salary_bonus = 1.5
    

    @property
    def incrementSalary(self):
        return self.salary * self.salary_bonus

    @incrementSalary.setter
    def incrementSalary(self , sai):
        self.salary_bonus = sai / self.salary

e = Emaployee()
print(e.incrementSalary)

e.incrementSalary = 6000
print(e.salary_bonus)
print(e.incrementSalary)


    
