from Employee import Employee
from Manager import Manager
from Executive import Executive

e1 = Employee("e1", 20, 20000)
m1 = Manager("m1", 20, 30000, "sales")
ex1 = Executive("ex1", 20, 40000, "sales", 10000)

e1.greetings()
m1.greetings()
ex1.greetings()

print(e1.totalSalary())
print(m1.totalSalary())
print(ex1.totalSalary())