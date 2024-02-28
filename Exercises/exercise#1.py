# 1. **Multiple Variable Assignment:**
#    Write a Python code to assign values '1', '4', and '3' to variables `a`, `b`, and `c` respectively in a single line.
a, b, c = '1', '4', '3'
print(a, b, c)

# 2. **String Length:**
#    Create a Python program to find the length of a given string `text` and print it.
text = "text"
print(f'Length of {text} is {len(text)}')

# 3. **List Manipulation:**
#    Write a Python script to add an element 'apple' to the end of a list `fruits`.
fruits = []
fruits.append("apple")
print(fruits)

# 4. **Dictionary Length:**
#    Write a Python code to find the number of key-value pairs in a dictionary `my_dict`.
car = { 
   'brand': 'Ford', 
   'model': 'Mustang', 
   'year': 2024 
}
print(f'Length of Dict {len(car)}')

# 5. **Global vs Local Variables:**
#    Define a global variable `x` outside a function and a local variable `x` inside a function. Print both variables to observe the scope difference.
x = "GLOBAL"

def my_function():
   x = "LOCAL"
   print(f'I am {x}')

def my_function_2():
   global x
   print(f'I am {x}')

print(f'I am {x}')
my_function()
my_function_2()