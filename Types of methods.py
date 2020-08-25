class iphone:
    color1='Black'
    color2='White'
    color3='Red'
    def __init__(self,c1,c2,c3):
        self.c1=c1
        self.c2=c2
        self.c3=c3
    def averageproduction(self):
        return self.c1+self.c2+self.c3/3

    @classmethod
    def iphonecolor(cls):
        return cls.color3

    @staticmethod
    def iphonemanufacturer():
        print('This Iphone desingned in California')

s1=iphone(27,20,74)
s2=iphone(47,21,25)
s3=iphone(15,63,36)

print(s1.averageproduction())
print(iphone.iphonecolor())
iphone.iphonemanufacturer()


