#simple calculator for addtion(x,y) substaction(x,y), multiplication(x,y) and division(x,y)
#let user call them interactively. modularize logic into functions

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error"
    return x / y

while True:
    print("\nSimple Calculator:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    ch = input("Enter your choice (1-5): ")

    if ch == "5":
        print("Exiting calculator...")
        break

    if ch in ("1", "2", "3", "4"):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if ch == "1":
            print("Result:", add(x, y))
        elif ch == "2":
            print("Result:", subtract(x, y))
        elif ch == "3":
            print("Result:", multiply(x, y))
        elif ch == "4":
            print("Result:", divide(x, y))
    else:
        print("Invalid choice! Please select 1-5.")

