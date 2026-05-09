print("Smart Calculator")
print("1.Additon")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = input("Choose your operation:")

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

if choice == "1":
    print(num1 + num2)

elif choice == "2":
    print(num1 - num2)

elif choice == "3":
    print(num1 * num2)

elif choice == "4":
    print(num1 / num2)


    
