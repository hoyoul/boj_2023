# 첫 번째 줄에는 문제의 정수 
# N이 주어진다. 
# 4<= N <= 1000

N = int(input())
if 4<= N <= 1000 and N%4 ==0:
    num_long = N //4
    print("long "*num_long, end='')
    print('int')
    
