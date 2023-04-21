import types
from inspect import ismethod

import os






def udfunc():
    print('udfunc called')
	
class Ten:
    def __get__(self, obj, objtype=None):
        return 10

class Person:
	
    y = Ten()
	
    def __init__(self):
        pass

    def objmethod(self):
        '''objmethod description'''
        print('obj method called')

    def objmethod2(self):
        '''objmethod2 description'''
        print('object method 2 called')

    # 這是 class method
    @classmethod
    def clsmethod(self):
        print('class method called')

print(Person.__dict__)

print('=================')		

		
# print(dir(udfunc))
print(udfunc)			# <function udfunc at ...>
print(type(udfunc))
#print(getmembers(udfunc))

print(ismethod(udfunc))				# False
print(Person.objmethod)	# <function Person.objmethod at ...>
print(ismethod(Person.objmethod))	# False
print(Person.objmethod2)# <function Person.objmethod2 at ...>
print(ismethod(Person.objmethod2))	# False
print(Person.clsmethod)	# <bound method Person.clsmethod of <class '__main__.Person'>>
print(ismethod(Person.clsmethod))	# True


print('測試 class 的 method')
f1 = Person().objmethod
print(type(f1)) # <class 'method'>
print(f1)   # <bound method Person.objmethod of <__main__.Person object at ...>>
print(isinstance(f1, types.MethodType))         # True
print(f1.__func__)                              # <function Person.objmethod at 0x000002D8D9B555A0>
print(f1())
print(f1.__func__(f1.__self__))    
print(' A... ')             # obj method called
f1.__self__.objmethod2()
print(' B... ')
#print(dir(f1))
# # ['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__func__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
# #
print(f1.__func__)

print(' .... ')

f2 = Person.objmethod
print(type(f2)) # <class 'function'>
print(f2)   # <function Person.objmethod at ...>
print(isinstance(f2, types.FunctionType))       # True
print(dir(f2))
# # ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


print(' 測試 class 的 class method ')
f3 = Person().clsmethod
print(type(f3))                                 # <class 'method'>
print(f3)   # <bound method Person.clsmethod of <class '__main__.Person'>>
print(isinstance(f3, types.MethodType))         # True
print(f3.__func__)                              # <function Person.clsmethod at ...>
print(f3.__self__)
# print(f3.__func__(f3.__self__))                 # class method called
# print(dir(f3))
# # ['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__func__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

print(' f4 ... ')

f4 = Person.clsmethod
print(type(f4))                                 # <class 'method'>
print(f4)   # <bound method Person.clsmethod of <class '__main__.Person'>>
print(isinstance(f4, types.MethodType))         # True
print(f4.__func__)                              # <function Person.clsmethod at ...>
print(f4.__self__)
# print(f4.__func__(f4.__self__))                 # class method called
# print(dir(f4))
print('end f4 ...')


print(f5 := Person().objmethod)
print(f6 := Person().objmethod)

for x in range(10):
	print(' ')

class DirectorySize:

    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute

s = Directory('songs')

print(dir(s))
print(dir())
print(locals(s))
		


