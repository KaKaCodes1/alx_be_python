num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case x if x == "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case x if x == "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case x if x == "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case x if x == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
