import sys

def printwithname(name):
    if len(name) == 0:
        name = ["World"]
    print("Hello", end = "")
    for i in name:
        print(" " + i, end = "")
    print("!")

name = sys.argv[1:]
printwithname(name)
