history = []

while True:
    print("\nSmart Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. View History")
    print("9. Exit")

    choice = input("Choose your operation: ")

    if choice == "8":
        print("\nCalculation History:")

        if len(history) == 0:
            print("No calculations yet.")

        else:
            for item in history:
                print(item)

        continue

    if choice == "9":
        print("Goodbye!")
        break

    if choice == "6":
        num1 = float(input("Enter a number: "))

    else:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

    if choice == "1":
        result = num1 + num2
        print("Result:", result)
        history.append(f"{num1} + {num2} = {result}")

    elif choice == "2":
        result = num1 - num2
        print("Result:", result)
        history.append(f"{num1} - {num2} = {result}")

    elif choice == "3":
        result = num1 * num2
        print("Result:", result)
        history.append(f"{num1} * {num2} = {result}")

    elif choice == "4":

        if num2 == 0:
            print("Cannot divide by zero")

        else:
            result = num1 / num2
            print("Result:", result)
            history.append(f"{num1} / {num2} = {result}")

    elif choice == "5":
        result = num1 ** num2
        print("Result:", result)
        history.append(f"{num1} ^ {num2} = {result}")

    elif choice == "6":

        if num1 < 0:
            print("Cannot find square root of a negative number")

        else:
            result = num1 ** 0.5
            print("Result:", result)
            history.append(f"√{num1} = {result}")

    elif choice == "7":
        result = (num1 / 100) * num2
        print("Result:", result)
        history.append(f"{num1}% of {num2} = {result}")

    else:
        print("Invalid choice")he second number:"))

    if choice == "1":
        print(num1 + num2)

    elif choice == "2":
        print(num1 - num2)

    elif choice == "3":
        print(num1 * num2)

    elif choice == "4":
        print(num1 / num2)

    else:
        print("Invalid choice")

    again = input("Do you want to continue? (y/n): ")

    if again == "n":
        break
