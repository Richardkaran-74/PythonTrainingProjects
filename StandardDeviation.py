import math

N = int(input().strip())
W = [int(i) for i in input().strip().split(' ')]

num = 0
for i in range(N):
    num += W[i]/N
num1 = 0
for i in range(N):
    num1 += (W[i]-num)**2/N
    q = math.sqrt(num1)
print(q)