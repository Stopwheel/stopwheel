def get_start_day(y, m):
    if m==1 or m==2:
        m+=12
        y-=1
    q=1 
    K=y%100 
    J=y//100  
    h=(q+(13*(m+1))//5+K+(K//4)+(J//4)-(2*J))%7
    day_of_week = (h + 5) % 7
    return day_of_week
print(get_start_day(2024, 2)) 