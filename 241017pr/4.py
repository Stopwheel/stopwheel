n = input("x=")
if n.startswith('0') and len(n) > 1:
    print("False")
else:
    a = int(n)
    b = a // 1000
    c = (a % 1000) // 100
    d = (a % 100) // 10
    e = a % 10

    if a < 0:
        print("False")
    elif 1 <= a <= 9:
        print("True")
    elif 10 <= a <= 99 and d == e:
        print("True")
    elif 100 <= a <= 999 and c == e:
        print("True")
    elif 1000 <= a <= 9999 and b == e and c == d:
        print("True")
    else:
        print("False")