




N = int(input().strip())
W = [int(i) for i in input().strip().split(' ')]
X = [int(i) for i in input().strip().split(' ')]


num = 0
for i in range(N):
    num += X[i]*W[i]
    Weigh = num/sum(X)
print(Weigh)