def countingValleys(s):
    valley = path = 0
    for step in s:
        if step == 'u':
            valley += 1
        else:
            valley -= 1
        if step == 'u' and valley == 0:
            path += 1
    return path


n = int(input())
s = input()
result = countingValleys(s)
print(result)