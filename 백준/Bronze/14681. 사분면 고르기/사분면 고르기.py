# 첫 줄에는 정수 x가 주어진다. 
# (−1000 ≤ x ≤ 1000; x ≠ 0) 다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)
X = int(input())
Y = int(input())
if -1000 <= X <= 1000 and X != 0 and -1000 <= Y <= 1000 and Y != 0:
    if X>0 and Y>0:
        print(1)
    elif X<0 and Y>0:
        print(2)
    elif X<0 and Y<0:
        print(3)
    else:
        print(4)