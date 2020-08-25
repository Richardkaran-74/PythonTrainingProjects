from functools import reduce
n=[20,27,74,47,63,36,18,81,72]
odd=list(filter(lambda n:n%2>0,n))
even=list(filter(lambda n:n%2==0,n))
print('odd:',odd)
print('Even:',even)
DoublO=list(map(lambda n:n*2,odd))
DoublE=list(map(lambda n:n*2,even))
print('DoublE:',DoublE)
print('DoublO:',DoublO)
compressO=reduce(lambda a,b:a+b ,DoublO)
compressE=reduce(lambda a,b:a+b ,DoublE)
print('compressO:',compressO)
print('compressE:',compressE)