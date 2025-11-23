a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(f"The sum is: {a + b}")

elif operation == "-":
    print(f"The difference is: {a - b}")

elif operation == "*":
    print(f"The product is: {a * b}")

elif operation == "/":
    if b != 0:
        print(f"The quotient is: {a / b}")

    else:
        print("Error: Division by zero is not allowed.")
         