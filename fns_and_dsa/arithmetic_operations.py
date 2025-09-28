def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num2 * num1
        case 'divide':
            if num2 == 0:
                print("you cannot divide by zero")
            else:
                return num1 / num2
        case _:
            print("Wrong operation selected.")