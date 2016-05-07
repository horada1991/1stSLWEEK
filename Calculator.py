#infinite loop
while 1:
    number1 = input("Enter a number (or a letter to" + "\033[1m" +
                " exit" + "\033[0m" + "): ")
    #IF there's any not_number character in the input,
    #then breaking the infinite while loop!
    if not number1.isdigit():
        break
    else:
        operation = input("Enter an operation: ")
        number2 = input("Enter another number: ")
        try:
            if operation == "+":
                print("Result:", int(number1) + int(number2), "\n")
            elif operation == "*":
                print("Result:", int(number1) * int(number2), "\n")
            elif operation == "-":
                print("Result:", int(number1) - int(number2), "\n")
            elif operation == "/":
                print("Result:", int(number1) / int(number2), "\n")
            else:
                #If there's no valid operation input, than write this
                print("Please enter a valid operation!\n")
        #Catch errors (ValueError: if the 'number2' contains letters too.)
        except:
            print("I can only do calculation with numbers! THANK YOU!\n")
