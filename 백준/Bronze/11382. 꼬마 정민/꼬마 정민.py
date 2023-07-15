#A, B, C (1 ≤ A, B, C ≤ 1012)
# 여러개의 변수의 true/false를 판별할때 and를 사용한다.
# 그리고 10의 12승은 pow()나 **를 사용한다.
A,B,C = list(map(int,input().split(' ')))
if 1<=A and A<10**12 and 1<=B and B<10**12 and 1<=C and C<10**12:
    print(A+B+C)
