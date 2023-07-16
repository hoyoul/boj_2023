# 첫째 줄에는 영수증에 적힌 총 금액 
# $X$가 주어진다.
# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 
# $N$이 주어진다.
# 이후 
# $N$개의 줄에는 각 물건의 가격 
# $a$와 개수 
# $b$가 공백을 사이에 두고 주어진다.
# 1 ≤ X ≤ 1,000,000,000
# 1 ≤ N ≤ 100 
# 1 ≤ a ≤ 1,000,000 
# 1 ≤ b ≤ 10 
X = int(input())
N = int(input())
if 1<= X <=1000000000 and 1<= N <=100:
    sum = 0
    for i in range(N):
        a,b = map(int, input().split(' '))
        sum = sum + a*b
    if sum != X:
        print("No")
    else:
        print("Yes")

