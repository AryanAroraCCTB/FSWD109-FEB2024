class Person:
    # Attributes
    name = ""
    age = 0

    # Initializer
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'Hi, I am {self.name}. I am {self.age} years old'

    # Methods
    # def greetings(self):
    #     print(f'Hi, I am {self.name}. I am {self.age} years old')

class Canadian:
    country = "Canada"

    def greetings(self):
        print(f'Hi, I am from {self.country}')

class Teacher(Person):
    year_joined = 0

    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year_joined = year

    # Method
    def my_school(self):
        print(f'I Teach at CCTB, I joined in {self.year_joined}')

class Student(Person, Canadian):
    year_joined = 0

    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year_joined = year

    # Method
    def my_school(self):
        print(f'I Study at CCTB, I joined in {self.year_joined}')

    # def greetings(self):
    #     print(f'Hi, I am STUDENT {self.name}. I am {self.age} years old')

person_1 = Person("xyz", 25)

student_1 = Student("abc", 20, 2024)
student_1.greetings()
student_1.my_school()

# teacher_1 = Teacher("def", 27)
# print(teacher_1)
# teacher_1.my_school()