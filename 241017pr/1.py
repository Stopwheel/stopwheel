total = 0
n = 0
while True:
    input_line = input()
    values = input_line.split()
    for val in values:
        if val == "-1":
            break
        elif not val.isdigit() or int(val) < 0 or int(val) > 100: 
            print("沒有輸入任何成績")
            continue
        total += int(val) 
        n += 1
    if "-1" in values:
        break
if n > 0:
    print(total / n) 
else:
    print("沒有輸入有效的成績")