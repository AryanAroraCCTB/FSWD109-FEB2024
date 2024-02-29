# Hard Questions:

# 11. **String Interpolation:**
#     Create a Python function named `format_string` that takes two parameters `name` and `age`. Use string interpolation to return a formatted string like "My name is [name] and I am [age] years old."

def format_string(name, age):
    return f'My name is {name} and I am {age} years old.'

print(format_string("XYZ", 20))

# 12. **Dictionary Manipulation:**
#     Write a Python code to remove the key-value pair where the key is 'age' from a dictionary `person`.

person = {
    "name": "xyz",
    "age": 20
}
print(person)
del person["age"]
print(person)

# 13. **Conditional with List:**
#     Given a list of numbers `numbers`, iterate through each number and print "Even" if it's even, and "Odd" if it's odd.

numbers = [1,2,3,4,5]
for num in numbers:
    if num % 2 == 0:
        print(num,"Even")
    else:
        print(num,"Odd")

# 14. **Loop with String:**
#     Write a Python program that takes a string `word` as input and prints each character of the string along with its index.

word = "word"
for index, character in enumerate(word):
    print(f'{character} on position {index}') 

for index in range(len(word)):
    character = word[index]
    print(f'{character} on position {index}') 
    
# 15. **Function with Variable Arguments:**
#     Define a Python function named `average` that takes a variable number of arguments and returns the average of all numebers the arguments passed.
    
def average(*args):
    sum = 0
    for num in args:
        sum += num
    print(sum/len(args))

average(1,2,3)
average(1,2,3,4,5,6)