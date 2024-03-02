class Employee:
    name = ""
    age = 0
    salary = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def greetings(self):
        print(f'Hi I am an Employee {self.name} of {self.age} years with {self.salary} salary per year.')

    def totalSalary(self):
        return self.salary
    
    def setSalary(self, new_salary):
        self.salary = new_salary