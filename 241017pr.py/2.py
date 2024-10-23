while True:
    print("\n選擇運算符號:")
    choice = input("請選擇運算符號（+,-,*,/): ")
    if choice not in ['+', '-', '*', '/']:
        print("無效的運算符號，請重新輸入")
        continue
    try:
        a = float(input("請輸入第一個數字："))
        if a == 999:
            print("程式結束")
            break
    except ValueError:
        print("無效的輸入，請輸入有效的數字")
        continue
    try:
        b = float(input("請輸入第二個數字："))
        if b == 999:
            print("程式結束")
            break
    except ValueError:
        print("無效的輸入，請輸入有效的數字")
        continue
    if choice == "+":
        print("結果: =", a ,"+",b,"=",a+b)
    elif choice == "-":
        print("結果: =", a ,"-",b,"=",a-b)
    elif choice == "*":
        print("結果: =", a ,"*",b,"=",a*b)
    elif choice == "/":
        if b == 0:
            print("不能除以 0,請重新輸入")
        else:
            print("結果: =", a ,"/",b,"=",a/b)