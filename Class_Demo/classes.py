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
    def greetings(self):
        print(f'Hi, I am {self.name}. I am {self.age} years old')

person_1 = Person("xyz", 25)
person_2 = Person("abc", 22)

# person_1.greetings()
# person_2.greetings()

print(person_1)
print(person_2)

del person_1.age

print(person_1)