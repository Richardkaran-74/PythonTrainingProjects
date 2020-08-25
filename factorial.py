def f(n):

    f=1

    for i in range(1,n+1):
        f=f*i
    return f

x=6

factorial=f(x)

print(factorial)