#472
#385
# 두개를 입력받아서 곱해서 더한결과를 출력한다.
#2360
#3776
#1416
#181720
fst_digit = input()
snd_digit = input()
fst_num = int(fst_digit)
snd_num = int(snd_digit)
fst_list = list(map(int,fst_digit))
snd_list = list(map(int,snd_digit))
sum = 0
num_length =3
if len(fst_list)==len(snd_list)==3:
    for i in range(len(fst_list)):
        num = fst_num*snd_list[num_length-(i+1)]
        print(num)
        num_digit= str(num)+'0'*i
        sum = sum + int(num_digit)
print(sum)
        






