#    *
#   ***
#  *****
# *******
#*********
# 첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ..., N번째 줄에는 별 2×N-1개를 찍는 문제
# 별은 가운데를 기준으로 대칭이어야 한다.
# 가운데를 기준으로 출력을 나눈다. end를 사용해서 left와 right를 출력하고 new line한다.

N = int(input())
T = 2*N -1
L = N
R = N -1
for i in range(N):
    print("%+{}s".format(L)%('*'*(i+1)),end='')
    print("%-{}s".format(i)%('*'*i))
    
    