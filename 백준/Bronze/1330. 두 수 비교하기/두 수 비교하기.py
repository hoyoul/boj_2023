#-10,000 ≤ A, B ≤ 10,000

A,B = list(map(int,input().split(' ')))
if -10000<=A and A <=10000 and -10000<=B and B <=10000:
    if A > B:
        print('>')
    elif A < B:
        print('<')
    else:
        print('==')