while True:
    print("\nChoose: add, subtract, multiply, divide, or quit")
    choice = input("Operation: ").lower().strip()

    if choice == "quit":
        break

    if choice not in ("add", "subtract", "multiply", "divide"):
        print("Please choose a listed operation.")
        continue

    first = float(input("First number: "))
    second = float(input("Second number: "))

    if choice == "add":
        answer = first + second
    elif choice == "subtract":
        answer = first - second
    elif choice == "multiply":
        answer = first * second
    elif choice == "divide":
        if second == 0:
            print("You can't divide by zero.")
            continue
        answer = first / second

    print("Answer:", answer)