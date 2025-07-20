a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")     
if operation == '+':
    print("Result:", a + b)
elif operation == '-':  
    print("Result:", a - b)
elif operation == '*':  
    print("Result:", a * b)
elif operation == '/':  
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed.")         