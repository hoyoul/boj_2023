#*****
# ****
#  ***
#   **
#    *
N = int(input())
if 1 <= N <=100:
    for i in range(N,0,-1):
        print("%{}s".format(N)%('*'*i))