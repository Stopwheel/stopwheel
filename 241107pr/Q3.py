def input_grades():
    grades = []
    while True:
        try:
            grade = int(input("請輸入成績(以負數結束):"))
            if grade < 0:
                break
            elif 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("成績必須在 0 到 100 之間，請重新輸入")
        except ValueError:
            print("請輸入有效成績")
    return grades
print('輸入的成績：', input_grades())
