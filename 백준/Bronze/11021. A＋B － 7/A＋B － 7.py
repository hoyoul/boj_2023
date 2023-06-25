T = int(input())

for i in range(T):
    A,B = map(int, input().split())
    if (A > 0) & (B < 10):
        number = i+1
        sum = A+B
        print("Case #{}: {}".format(number,sum))