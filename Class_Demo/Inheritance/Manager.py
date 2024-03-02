from Employee import Employee

class Manager(Employee):
    department = ""

    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department