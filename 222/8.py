while True:
    print("1.系所")
    print("2.算術運算")
    print("3.畫迴圈三角形")
    print("q.quit")
    choice=input("Enter you choice:")
    if choice=="1":
        print("AITA")
    elif choice =="2":
        a,op,b=input("Enter you choice:").split()
        a=float(a)
        b=float(b)
        if op =="+":
            print(a+b)
        elif op == "-":
            print(a-b)
        elif op == "*":
            print(a*b)
        elif op == "/":
            print(a/b)
        else:
            print("Invalid operator")
    elif choice =="3":
        n=3
        for i in range(n):
            for j in range (n-i-1):
                print(" ",end="")
            for k in range(2*i+1):
                print("*",end="")
            print()
    elif choice =="q":
        break