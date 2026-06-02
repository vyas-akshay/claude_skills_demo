def modulo(a, b):
    return a % b   # Still missing zero check — Claude will catch this!

def calculate(operation, a, b):
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        return divide(a, b)
    elif operation == "modulo":
        return modulo(a, b)
    else:
        print("Unknown operation")

while True:
    a = float(input("Enter first number: "))
    op = input("Operation: ")
    b = float(input("Enter second number: "))
    print("Result:", calculate(op, a, b))
    if input("Continue? (y/n): ") != "y":
        break