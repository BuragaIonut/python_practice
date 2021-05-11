


class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def work(self):
        print(f'{self.name} is working ...')


class SoftwareEngineer(Employee):
    def __init__(self, name, age, level, salary):
        super().__init__(name,age,salary)
        self.level = level

    
    def debug(self):
        print(f'{self.name} is debuging ... and he gets {self.salary} $$$')



class Designer(Employee):
    pass



se = SoftwareEngineer('Mihai', 22, 'Junior', 2500)

d = Designer('John', 24, 4000)

print(se.salary, se.level)
print(se.debug())
