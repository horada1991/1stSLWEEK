import sys

def printwithname(name = [" World"]):
    print("Hello", end = "")
    for i in name:
        print(" " + i, end = "")
    print("!")

name = sys.argv[1:]
printwithname() if len(name) == 0 else printwithname(name)
