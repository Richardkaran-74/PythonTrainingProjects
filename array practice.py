from array import *

Ric=array('i',[])

r=int(input('Enter the lenght of array:'))

for i in range(r):
     x=int(input('Enter the value:'))
     Ric.append(x)

print(Ric)

abc=int(input('Enter the value for search:'))

b=0
for e in Ric:
        if e==abc:
            print(b)
            break
        b+=1
else:
    print('not found')


print(Ric.index(abc))
