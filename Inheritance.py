class A:
    def __init__(self):
        print('A')
    def feature1(self):
        print('Update 1 is working')
    def feature2(self):
        print('Update 2 is working')
class B():
    def __init__(self):
          print('B')
    def feature2(self):
        print('Update 3 is working')
    def feature3(self):
        print('Update 4 is working')
class C(A,B):
    def __init__(self):
        super().__init__()
        print('C')

a=C()
a.feature2()
