def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."


while True:

    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("Q. Quit")

    choice = input("Enter choice (1/2/3/4 or Q): ")

    # Quit the calculator
    if choice.lower() == 'q':
        print("Calculator closed.")
        break

    # Check whether the choice is valid
    if choice in ['1', '2', '3', '4']:

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {add(num1, num2)}")

            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")

            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")

            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or Q.")

