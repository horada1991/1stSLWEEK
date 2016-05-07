import sys

#funct of Print, with command line arguments
def PrintWithName(name):
    print("Hello", end = "")
    for i in name:
        print(" " + i, end = "")
    print("!")

PrintWithName(sys.argv[1:]) if sys.argv[1:] else print("Hello World!")

#It could be solved in one logical line by the .join funct
# but you asked for a new definied funct :D
