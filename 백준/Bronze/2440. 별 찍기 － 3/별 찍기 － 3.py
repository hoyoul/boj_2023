#첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# print할때 format()와 %()를 사용하는법
# 여기서 주의해야 할께, format(N)을 사용할 수도 있다. 여기선 format(i)를 사용해서 해결했다.

N = int(input())
if 1<= N <=100:
    for i in range(N,0,-1):
        print("%-{}s".format(i)%('*'*i))

