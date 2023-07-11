m,d = input().split(' ')
date = ['SUN','MON','TUE','WED','THU','FRI','SAT']
month = [31,28,31,30,31,30,31,31,30,31,30,31]
days = 0 
for i in range(int(m)-1):
    days = days + month[i]
total_days = days + int(d)
print(date[total_days % 7])
    
    