n = int(input("請輸入一個正整數: "))
if n < 1:
    print("請輸入一個有效的正整數")
else:
    k = 1
    for i in range(1, n+1):
        k*= i
    print(n, "! =", k)