#첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# print시 string객체의 format()를 사용해서 string객체에 입력이 가능할 수도 있지만, %()를 통해서
# string객체에 대한 처리도 가능
N = int(input())
if 1<= N <= 100:
    for i in range(1,N+1):
        print("%{}s".format(N)%('*'*i))
