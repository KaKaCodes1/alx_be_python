def perform_operation(num1,num2,operation):
    match operation:
        case x if x == 'add':
            return num1 + num2
        case x if x == 'subtract':
            return num1 - num2
        case x if x == 'multiply':
            return num2 * num1
        case x if x == 'divide':
            if num2 == 0:
                print("you cannot divide by zero")
            else:
                return num1 / num2
        case _:
            print("Wrong operation selected.")