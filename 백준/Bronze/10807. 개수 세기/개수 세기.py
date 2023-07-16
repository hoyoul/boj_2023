N = int(input())
l1 = list(map(int, input().split(' ')))
v = int(input())
count = 0
for i in range(len(l1)):
    if v == l1[i]:
        count = count +1
print(count)
        

