result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number:
        user_input = input("Enter a number or = to calculate: ")
        if user_input == '=':
            if result is not None and operator is not None and operand is not None:
                if operator == '+':
                    result += operand
                elif operator == '-':
                    result -= operand
                elif operator == '*':
                    result *= operand
                elif operator == '/':
                    if operand != 0:
                        result /= operand
                    else:
                        print("Division by zero is not allowed. Try again.")
                        continue
                else:
                    print(f"Invalid operator: {operator}. Try again.")
                    continue
                print(f"Result: {result}")
                break
            else:
                print("Invalid input. Try again.")
                continue
        try:
            operand = float(user_input)
        except ValueError:
            print(f"'{user_input}' is not a valid number. Try again.")
            continue
        wait_for_number = False
    else:
        user_input = input("Enter an operator (+, -, *, /): ")
        if user_input in ('+', '-', '*', '/'):
            operator = user_input
            wait_for_number = True
        else:
            print(f"Invalid operator: {user_input}. Try again.")

