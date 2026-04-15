test = True

while test:
    print("a. addition")
    print("b. soustraction")
    print("c. multiplication")
    print("d. division")
    print("q. quit")
    choice = input("Enter your choice: ")
    match choice:
        case "a":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = a + b
            print(result)
        case "b":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = a - b
            print(result)
        case "c":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = a * b
            print(result)
        case "d":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if b == 0 :
                print("impossible")
            else:
                result = a / b
                print(result)
        case "q":
            test = False
        case _:
            print("invalid choice")