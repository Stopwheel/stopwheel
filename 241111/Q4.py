import sys

def fun(n):
    if n == 1:
        return 1
    else:
        return n * fun(n - 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Wrong input")
    else:
        print(fun(int(sys.argv[1])))
