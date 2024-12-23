import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Wrong input")
    else:
        key = int(sys.argv[2])
        out = []
        for c in sys.argv[3]:
            if sys.argv[1] == "Enc":
                out.append(chr(ord(c) + key))
            elif sys.argv[1] == "Dec":
                out.append(chr(ord(c) - key))
        print("".join(out))
