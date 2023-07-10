s = input()
l = len(s)
if (l > 0) & (l< 100):
    p = l // 10
    q = l % 10
    if q != 0:
        p += 1
    for i in range(p):
        print(s[i*10:(i+1)*10])