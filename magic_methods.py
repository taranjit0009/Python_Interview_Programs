import inspect
def magic_method(a='b',d=True):
    print(dir(int))
magic_method()
sign = inspect.signature(magic_method)
print(sign)


for x in sign.parameters.values():
    print(x.name,x.annotation,x.kind)

class A:
    def par(d=2):
        print('parent call method.')
objA= A()
objA.par()

class C(A):
    def par(self,c=3):
        print('child class overloading method.')

objC = C()
objC.par()