class person:
    def __init__(self):
        self.name='Richard'
        self.age=24

    def compare(self,other):
        if len(self.name)==len(other.name):
            return True
        else:
            return False

c1=person()
c2=person()

c2.name='Brindha'

if c1.compare(c2):
    print('Same')
else:
    print('Different')

print(c1.name)
print(c2.name)