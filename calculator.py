# Simple Calculator
# A basic command-line calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b   # Bug: no zero division check

def calculate(operation, a, b):
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        return divide(a, b)
    else:
        print("Unknown operation")  # Bad: no return value

# No input validation, no type hints, no docstrings
a = float(input("Enter first number: "))
op = input("Enter operation (add/subtract/multiply/divide): ")
b = float(input("Enter second number: "))

result = calculate(op, a, b)
print("Result:", result)
