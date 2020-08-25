
def mean(data):
    return sum(data)/len(data)


def median(sample):
    n = len(sample)
    index = n // 2
    if n % 2:
        return sorted(sample)[index]
    return sum(sorted(sample)[index - 1:index + 1]) / 2


def mode(arr):
    counts = []
    for i in arr:
        counts.append(arr.count(i))
    if max(counts) > 1:
        print(arr[counts.index(max(counts))])
    else:
        print(min(arr))

N = int(input().strip())

arr = [int(i) for i in input().strip().split(' ')]

m = mean(arr)
print(m)

p = median(arr)
print(p)

r = mode(arr)
