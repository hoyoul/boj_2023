# 4개의 조각으로 나눠서 처리한다. N은 Level을 나타내는데, N보다 2배의 Level을 갖는다.
N = int(input())
T = 2*N -1
L = N
R = N -1
for i in range(T):
    if i < N:
        print("%-{}s".format(L)%('*'*(i+1)),end='')
        print("%+{}s".format(L)%('*'*(i+1)))
    else:
        print("%-{}s".format(L)%('*'*(T-i)),end='')
        print("%+{}s".format(L)%('*'*(T-i)))        
