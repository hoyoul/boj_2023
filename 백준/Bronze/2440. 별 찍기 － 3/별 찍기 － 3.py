#첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# print할때 format()와 %()를 사용하는법

N = int(input())
if 1<= N <=100:
    for i in range(N,0,-1):
        print("%-{}s".format(i)%('*'*i))

