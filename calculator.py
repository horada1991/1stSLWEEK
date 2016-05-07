import operator

operators = {"+" : operator.add, "-" : operator.sub,
            "*" : operator.mul, "/" : operator.truediv}

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
            print(operators[operation](int(number1), int(number2)))
        #Catch KeyErrors (No valid opertion given)
        except KeyError:
            print("Please enter a valid operation!\n")
        #if the 'number2' contains letters too.
        except ValueError:
            print("I can only do calculation with numbers! THANK YOU!\n")
