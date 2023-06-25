while True:
    A,B = map(int, input().split())
    if A == 0 & B ==0:
        break
    elif A>0 & B<10:
        print(A+B)
