def step(n):
    steps = 0
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        steps += 1
    return sequence, steps
try:
    n = int(input("請輸入一個正整數："))
    if n <= 0:
        print("請輸入一個正整數！")
    else:
        sequence, steps = step(n)
        print(" -> ".join(map(str, sequence)))
        print("總共步數：", steps)
except ValueError:
    print("請輸入有效的正整數。")