def count(list):
    Great=0

    for i in list:
        if len(i)>5:
            Great+=1
            print('Great than five letter names:{}'.format(i))

    return Great



lst=('muthu','prakash','martin','vishnu','jana','kanal','bala','prince','richard','brindha')

Great=count(lst)


arr=[]
n=10
for i in range(n):
    x=input("enter the name")
    arr.append(x)
print(arr)

cnt=0
for j in (arr):
    if(len(j)>5):
        print("name:{},length:{}".format(j,len(j)))
        cnt+=1
print("Total number of names with length more than 5 is:" ,cnt)


