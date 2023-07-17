N,X = map(int, input().split(' '))
A = list(map(int,input().split(' ')))
temp = list(filter(lambda a: a < X, A ))
for i in range(len(temp)):
    print(temp[i],end=' ')

