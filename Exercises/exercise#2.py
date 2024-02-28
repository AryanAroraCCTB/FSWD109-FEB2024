# Medium Questions: 

# 6. **String Slicing:**
#    Given a string `sentence`, extract the first five characters and print them.
sentence = "sentence"
print(sentence[0:5])
print(sentence[:5])
print("===========")
 
# 7. **List Operations:**
#    Perform the following operations on a list `numbers`:
#    - Append the number '10'.
#    - Remove the number '5'.
#    - Print the final list.
numbers = [1,2,3,4,5,6,7]
numbers.append(10)
numbers.remove(5)
print(numbers)
print("===========")

# 8. **Dictionary Operations:**
#    Consider a dictionary `person` with keys 'name', 'age', and 'city'. Print all the key-value pairs using a loop.
person = {
    'name': "person_name",
    'age': 20,
    'city': "vancouver"
}
for key in person:
    print(f'{key} is {person[key]}')

for key in person.keys():
    print(f'{key} is {person[key]}')

for item in person.items():
    print(f'{item[0]} is {item[1]}')

for key, value in person.items():
    print(f'{key} is {value}')

print("===========")

# 9. **Boolean Evaluation:**
#    Check if the variable `num` is greater than 10. If it is, print "Greater than 10"; otherwise, print "Less than or equal to 10".
num = 11
if num > 10:
    print("Greater than 10")
else:
    print("Less than 10")

print("Greater than 10") if num > 10 else print("Less than 10")

print("===========")

# 10. **Function with Default Parameter:**
#     Write a Python function named `greet` that takes a parameter `name` with a default value of "Guest". The function should print "Hello, [name]!" where [name] is replaced with the value passed or the default value if none is provided.
def greet(name = "Guest"):
    print(f'Hello {name}')

greet("Aryan")
greet()

print("===========")