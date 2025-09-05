from datetime import datetime

def calculate(a, b, op):
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                return "Error: Division by zero"
            return a / b
        else:
            return "Error: Invalid operator"
    except Exception as e:
        return f"Error: {str(e)}"

while True:
    print("\n--- Calculator ---")
    print("1. Calculate")
    print("2. Exit")
    choice = input("Choose: ")

    if choice == "1":
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Enter operator (+, -, *, /): ")
            result = calculate(a, b, op)
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Result: {result} (Time: {time})")
        except ValueError:
            print("Error: Please enter valid numbers.")
    elif choice == "2":
        break
    else:
        print("Invalid choice. Try again.")
