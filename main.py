#Math Magician Main File
#usage: math operator operand1 operand2
def main(): 
    import sys
    print("Welcome to math magigician")

    op = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])


def divise(a, b):
    if b == 0:
        print("doesnt work")
    return a / b    

if __name__ == "__main__":
    main()