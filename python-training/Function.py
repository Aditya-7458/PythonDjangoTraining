# Function- a function is a block of organized, reusable code that performs a specific task.
# Functions provide modularity and help in organizing code by breaking it into smaller, manageable pieces.


def add(num1,num2):
    return num1+num2    # this is function 

result=add(10,4)
print(result)



# We have built in function as well as user defined function.


## Calculator 

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")

    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")

    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")

    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

    else:
        print("Invalid input")

calculator()


    