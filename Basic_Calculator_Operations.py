num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Select operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print(f"{num1} + {num2} = {num1 + num2}")

elif choice == '2':
    print(f"{num1} - {num2} = {num1 - num2}")

elif choice == '3':
    print(f"{num1} * {num2} = {num1 * num2}")

elif choice == '4':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("You want to perform the division operation but the second number you entered is 0")
        print("Error: Division by zero is not allowed.")

else:
    print(f"{choice} is not valid choice. Enter the digits between 1 to 4.")