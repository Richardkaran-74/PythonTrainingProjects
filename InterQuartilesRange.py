def med(list):
    list.sort()
    n = len(list)//2
    if len(list)%2:
        return sorted(list)[n]
    return sum(sorted(list)[n-1:n+1])/2

N = int(input().strip())

arr1 = [int(i) for i in input().strip().split(' ')]
arr2 = [int(i) for i in input().strip().split(' ')]

arr = []
for i in range(N):
    for j in range(arr2[i]):
        arr.append(arr1[i])

q2 = med(arr)

lower = [i for i in arr if i < q2]
upper = [i for i in arr if i > q2]

q1 = med(lower)
q3 = med(upper)

result = q3 - q1
print(result)
