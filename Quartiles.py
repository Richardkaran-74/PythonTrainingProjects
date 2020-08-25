def median(data):
    data.sort()
    n = len(data)//2
    if len(data)%2:
        return sorted(data)[n]
    return sum(sorted(data)[n-1:n+1])/2


N = int(input().strip())

arr = [int(i) for i in input().strip().split(' ')]

q2 = median(arr)

lowermedian = [i for i in arr if i < q2]
uppermedian = [i for i in arr if i > q2]

q1 = median(lowermedian)
q3 = median(uppermedian)

print(int(q1))
print(int(q2))
print(int(q3))