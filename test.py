import logging

logging.basicConfig(level=logging.INFO)

class LoggedAgeAccess:
    
    def __init__(self):
        print('LoggedAgeAccess __init__')
    
    def __get__(self, obj, objtype=None):
        print('LoggedAgeAccess __get__')
        value = obj._age
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, obj, value):
        print('LoggedAgeAccess __set__')
        logging.info('Updating %r to %r', 'age', value)
        obj._age = value

class Person:

    age = LoggedAgeAccess()             # Descriptor instance
    team = 'Mavs'
    
    officer = 'D'

    def __init__(self, name, age):
        print('Person __init__')
        print(type(self))
        self.name = name                # Regular instance attribute        
        #self.age = age                  # Calls __set__()

    def birthday(self):
        self.age += 1                   # Calls both __get__() and __set__()
    
mary = Person('Mary M', 30)             # The initial age update is logged
# mary.team = 'Lakers'
print(vars(mary))
mary.age = 40
print(mary.age)
print(vars(mary))
# INFO:root:Updating 'age' to 30
# >>> dave = Person('David D', 40)
# INFO:root:Updating 'age' to 40
# Person.__dict__['age'] = '999'
# print(Person.__dict__)
# print(dir(mary))                          # The actual data is in a private attribute
# print(vars(mary))                          # The actual data is in a private attribute
# {'name': 'Mary M', '_age': 30}
# >>> vars(dave)
# {'name': 'David D', '_age': 40}

# >>> mary.age                            # Access the data and log the lookup
# INFO:root:Accessing 'age' giving 30
# 30
# >>> mary.birthday()                     # Updates are logged as well
# INFO:root:Accessing 'age' giving 30
# INFO:root:Updating 'age' to 31

# >>> dave.name                           # Regular attribute lookup isn't logged
# 'David D'
# >>> dave.age                            # Only the managed attribute is logged
# INFO:root:Accessing 'age' giving 40
# 40

import types

class Funcs(object):
        
    def __call__(self, *args, **kwargs):
        pass
        # print('called')
    
    def __get__(self, obj, objtype=None):
        pass
        # print("Simulate func_descr_get() in Objects/funcobject.c")
        if obj is None:
            return self
        # print(self)
        # print('obj=', obj)
        return types.MethodType(self, obj)

class Home:
    
    def __init__(self):
        pass

    def buyGrocery(self, stuff):
        pass
		# print('I bought with' ,  self)

def f(obj):
    pass
	# print('I am called from', obj)

a = Home()

# print(type(Home.buyGrocery)) # <class 'function'>
# print(Home.buyGrocery) # <function Home.buyGrocery at 0x000001B12FF5BD00>
# print(type(a.buyGrocery)) # <class 'method'>
# print(a.buyGrocery) # <bound method Home.buyGrocery of <__main__.Home object at 0x000001B12FF3FD30>>

a.func = f

# print(a.func) # <function f at 0x000001B12FE33E20>
# print(type(a.func)) # <class 'function'>

a.func = types.MethodType(f, a)

# print(a.func) # <function f at 0x000001B12FE33E20>
# print(type(a.func)) # <class 'function'>

#a.func()

# # print(type(a.buyGrocery('banana')))
	




		
# p = Home()
# # print(types.MethodType(p, p.buyGrocery))

# class Test:
    
    # y = Xunction()
    
    # def __init__(self, x):
        # # print(callable(self.y))
        # self._x = x
    
    # def moose(self, value):
        # # print(self._x + value)
        

# t = Test(20)
#t.x(30)
