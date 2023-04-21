import types

class Funcs(object):
        
    def __call__(self, *args, **kwargs):
        print('called')
    
    def __get__(self, obj, objtype=None):
        print("Simulate func_descr_get() in Objects/funcobject.c")
        if obj is None:
            return self
        print(self)
        print('obj=', obj)
        return types.MethodType(self, obj)

class Home:
    
	def __init__(self):
		pass

	def buyGrocery(self, stuff):
		print('I bought with' ,  self)

def f(obj):
	print('I am called from', obj)

a = Home()

print(type(Home.buyGrocery)) # <class 'function'>
print(Home.buyGrocery) # <function Home.buyGrocery at 0x000001B12FF5BD00>
print(type(a.buyGrocery)) # <class 'method'>
print(a.buyGrocery) # <bound method Home.buyGrocery of <__main__.Home object at 0x000001B12FF3FD30>>

a.func = f

print(a.func) # <function f at 0x000001B12FE33E20>
print(type(a.func)) # <class 'function'>

a.func = types.MethodType(f, a)

print(a.func) # <function f at 0x000001B12FE33E20>
print(type(a.func)) # <class 'function'>

#a.func()

# print(type(a.buyGrocery('banana')))
	




		
# p = Home()
# print(types.MethodType(p, p.buyGrocery))

# class Test:
    
    # y = Xunction()
    
    # def __init__(self, x):
        # print(callable(self.y))
        # self._x = x
    
    # def moose(self, value):
        # print(self._x + value)
        

# t = Test(20)
#t.x(30)
