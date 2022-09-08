while True:
    def add(a, b):
        answer = a + b
        print(f"{str(a)} + {str(b)} = {str(answer)}")

    def sub(a, b):
        answer = a - b
        print(f"{str(a)} - {str(b)} = {str(answer)}")

    def div(a, b):
        answer = a / b
        print(f"{str(a)} / {str(b)} = {str(answer)}")

    def mul(a, b):
        answer = a * b
        print(f"{str(a)} * {str(b)} = {str(answer)}")

    print("A. Addition")
    print("B. Subtraction")
    print("C. Division")
    print("D. Multiplication")
    print("E. Exit")

    choice = input("Your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("First Number: "))
        b = int(input("Second Number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("First Number: "))
        b = int(input("Second Number: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Division")
        a = int(input("First Number: "))
        b = int(input("Second Number: "))
        div(a, b)
    elif choice == "d" or choice == "D":
        print("Multiplication")
        a = int(input("First Number: "))
        b = int(input("Second Number: "))
        mul(a, b)
    elif choice == "e" or choice == "E":
        print("Process Ended")
        quit()
