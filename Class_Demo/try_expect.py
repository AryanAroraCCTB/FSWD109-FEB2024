import math

while True:
    x = int(input("Enter value: "))

    if x > 100:
        print("Bye...")
        break

    y = math.sqrt(x)

    print(f'You entered {x}, sqrt is {y}')