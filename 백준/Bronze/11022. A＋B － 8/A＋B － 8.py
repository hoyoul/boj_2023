T = int(input())
for i in range(T):
    A,B = map(int, input().split())
    C = A+B
    num = i+1
    if(A>0) & (B<10):
        print("Case #{}: {} + {} = {}".format(num,A,B,C))