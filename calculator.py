<<<<<<< HEAD
#infinite loop
while 1:                        #infinite loop
    number1 = input("Enter a number (or a letter to" + "\033[1m" + " exit" + "\033[0m" + "): ")
    if not number1.isdigit():
        #IF there's any not_number character in the input than breaking the infinite while loop!
        break
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
            #If there's no valid operation input than write this
            print("Please enter a valid operation!")
