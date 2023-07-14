# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 
# 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 
#모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

N = int(input())
L = list(map(int, input().split(' ')))
min = 1000000
max = -1000000
for i in range(N):
    if L[i] > max:
        max = L[i]
    if L[i] < min:
        min = L[i]
print(min,max)
