# 예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 
# 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다.
# 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.
# for-loop은 가능성의 공간을 의미한다. 3개의 for-loop을 사용해야 한다. 그런데 이경우는 
# 가능성의 공간에서의 어떤 결정이 아닌, 이미 결정된 값에 대한 처리다. 두개의 처리는 다르다. 
total =0
eye1,eye2,eye3 = map(int,input().split(' '))
if 1<= eye1 <=6 and 1<= eye2 <=6 and 1<= eye3 <=6:
    if eye1 == eye2 == eye3:
        total = 10000 + eye1*1000
    elif eye1 == eye2 or eye2 == eye3 or eye1 == eye3:
        if eye1 == eye2:
            total = 1000 + eye1*100
        else:
            total = 1000 + eye3* 100
    else:
        maxvalue = max(eye1,eye2,eye3)
        total = maxvalue*100
print(total)
        
