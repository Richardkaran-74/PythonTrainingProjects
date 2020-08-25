
def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


p = int(input())
for i in range(p):
    num = int(input())
    if check_prime(num):
        print('Prime')
    else:
        print('Not prime')
