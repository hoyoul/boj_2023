# 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다.
# 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.

A,B = map(int,input().split(' '))
C = int(input())
if 0<= A<= 23 and 0<=B <=59 and 0<=C <=1000:
    C_H = C // 60
    C_M = C % 60
    M = C_M + B
    if M < 60:
        H = (A + C_H) % 24
        print(H,M)
    else:
        AH = M // 60
        M = M % 60
        H = (A + C_H +AH) % 24
        print(H,M)
        