import sys
lines = sys.stdin.readlines()
for line in lines:
    A,B = map(int, line.split())
    if (A>0) & (B<10):
        print(A+B)