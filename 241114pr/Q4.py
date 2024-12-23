def is_leap_year(y):
    return (y% 4==0 and y%100!=0) or (y%400==0)
def get_days_in_month(y,m):
    if m == 2:
        return 29 if is_leap_year(y) else 28
    elif m in [4, 6, 9, 11]:
        return 30
    else:
        return 31
def get_start_day(y,m):
    if m==1 or m==2:
        m+=12
        y-=1
    q=1 
    K=y%100 
    J=y//100 
    h=(q+(13*(m+1))//5+K+(K//4)+(J//4)-(2*J))%7
    day_of_week=(h+5)%7
    return day_of_week
def display_calendar(y, m):
    print(f"     {y}年 {m}月")
    print("Mo Tu We Th Fr Sa Su")
    days_in_month=get_days_in_month(y,m)
    start_day=get_start_day(y,m)
    print("   " * start_day, end="")
    for day in range(1, days_in_month + 1):
        print(f"{day:2}", end=" ")
        if (start_day + day) % 7 == 0:
            print()
    print() 
display_calendar(2024,11)