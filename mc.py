print("===================================")
print("   MATHEMATICAL CALCULATOR (MC)")
print("===================================")

while True:
    print("\nChoose an Operation")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("%  Modulus")
    print("^  Power")
    print("C  Clear")
    print("OFF  Exit")

    choice = input("\nEnter your choice: ").upper()

    if choice == "OFF":
        print("Calculator Closed.")
        break

    elif choice == "C":
        print("Calculator Cleared.")
        continue

    elif choice in ["+", "-", "*", "/", "%", "^"]:

        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == "+":
            result = num1 + num2

        elif choice == "-":
            result = num1 - num2

        elif choice == "*":
            result = num1 * num2

        elif choice == "/":
            if num2 == 0:
                print("Error! Cannot divide by zero.")
                continue
            result = num1 / num2

        elif choice == "%":
            result = num1 % num2

        elif choice == "^":
            result = num1 ** num2

        print("Result =", result)

    else:
        print("Invalid choice. Try again.")
