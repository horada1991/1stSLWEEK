import sys

#funct of Print, with command line arguments
def printwithname(name):
    print("Hello", end = "")
    for i in name:
        print(" " + i, end = "")
    print("!")

#Slicing down the name of the script
name = sys.argv[1:]
print("Hello World!") if len(name) == 0 else printwithname(name)
