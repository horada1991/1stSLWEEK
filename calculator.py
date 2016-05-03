while 1:                                #infinite loop
    number1 = input("Enter a number (or a letter to" + "\033[1m" + " exit" + "\033[0m" + "): ")
    if not number1.isdigit():
        break                           #IF there's any letter in the input than breaking the infinite while loop!
    else:
        operation = input("Enter an operation: ")
        number2 = input("Enter another number: ")
        if operation == "+":
            print(int(number1) + int(number2))
        elif operation == "*":
            print(int(number1) * int(number2))
        elif operation == "-":
            print(int(number1) - int(number2))
        elif operation == "/":
            print(int(number1) / int(number2))
        else:
            print("Please enter a valid operation!")    #If there's no valid operation input than write this
