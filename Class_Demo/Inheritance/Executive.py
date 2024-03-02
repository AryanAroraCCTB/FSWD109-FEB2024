from Manager import Manager

class Executive(Manager):
    bonus = 0

    def __init__(self, name, age, salary, department, bonus):
        super().__init__(name, age, salary, department)
        self.bonus = bonus

    def totalSalary(self):
        return super().totalSalary() + self.bonus