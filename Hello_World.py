import sys

#funct of Print, with command line arguments
def printwithname(name):
    print("Hello", end = "")
    for i in name:
        print(" " + i, end = "")
    print("!")

name = sys.argv[1:]             #Slice down the name of the script
if len(name) == 0:              #If there's no elements in tha list called name
    print("Hello World!")
else:
    printwithname(name)
