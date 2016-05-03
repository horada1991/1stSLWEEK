import sys

#funct of Print, with command line arguments
def printwithname(name):
    print("Hello", end = "")
    for i in name:
        print(" " + i, end = "")
    print("!")

name = sys.argv[1:]      #Slice down the name of the script
print("Hello World!") if len(name) == 0 else printwithname(name)
