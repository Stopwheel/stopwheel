import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Wrong input")
    else:
        op = sys.argv[2]
        if op == "+":
            print(int(sys.argv[1]) + int(sys.argv[3]))
        elif op == "-":
            print(int(sys.argv[1]) - int(sys.argv[3]))
        elif op == "*":
            print(int(sys.argv[1]) * int(sys.argv[3]))
