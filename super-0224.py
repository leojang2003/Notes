from pprint import pprint 
# super() 的用途是在解決 inheritance diamond 用的
# 也就是
#     A
#    / \
#   B   C
#    \ /
#     D 

# 如果沒有 super() 的情況下 

class A:
    def __init__(self):
        print('A.__init__')
        super(A, self).__init__()
        
class B(A):
    def __init__(self):
        print('B.__init__')        
        A.__init__(self)    # 沒有呼叫 super() 直接呼叫 A.__init__()  
        
        
class C(A):
    def __init__(self):
        print('C.__init__')
        super(C, self).__init__()
   
class D(B, C):
    def __init__(self):
        print('D.__init__')
        super(D, self).__init__()

pprint(D.__mro__)
# (<class '__main__.D'>,
#  <class '__main__.B'>,
#  <class '__main__.C'>,
#  <class '__main__.A'>,
#  <class 'object'>)
#
# 所以 MRO 順序為 D - B - C - A
        
d = D()
# D.__init__
# B.__init__
# A.__init__
# 因為 class B 的 __init__ 沒有呼叫 super() 所以我們可看到 class C 的 __init__ 沒有呼叫到

class A:
    def __init__(self):
        print('A.__init__')
        super(A, self).__init__()
        
class B(A):
    def __init__(self):
        print('B.__init__')        
        A.__init__(self) 
        # 沒有呼叫 super() 直接呼叫 A.__init__()
        
class C(A):
    def __init__(self):
        print('C.__init__')
        super(C, self).__init__()

# 調整繼承的順序，B        
class D(C, B):
    def __init__(self):
        print('D.__init__')
        super(D, self).__init__()

pprint(D.__mro__)
# (<class '__main__.D'>,
#  <class '__main__.C'>,
#  <class '__main__.B'>,
#  <class '__main__.A'>,
#  <class 'object'>)

d = D()
# D.__init__
# C.__init__
# B.__init__
# A.__init__

# 如果我們調整 class D 的繼承順序，改成 C、B，則 MRO 變成 D - C - B - A 
# 剛好沒問題。為了避免一開始的情況，class B 要改成呼叫 super().__init__() 如下

class A:
    def __init__(self):
        print('A.__init__')
        super(A, self).__init__()
        
class B(A):
    def __init__(self):
        print('B.__init__')        
        super(B, self).__init__()
        
class C(A):
    def __init__(self):
        print('C.__init__')
        super(C, self).__init__()
   
class D(B, C):
    def __init__(self):
        print('D.__init__')
        super(D, self).__init__()

d = D()

# super() 的 signature 如下
# class super(type, object_or_type=None)
# super()回傳一個 proxy object 委派 method call 給 type 的 parent 或 sibling class
# object_or_type 決定 MRO 找尋的順序，會從 object_or_type 下一個 class 開始
   
class D(B, C):
    def __init__(self):
        print('D.__init__')      
        super(B, self).__init__()

print(D.__mro__)
# MRO D > B > C > A > object
d = D()
# 因為我們在 D 的 __init__ 呼叫 super(B, self).__init__()，所以在 MRO 中，會呼叫 B class 的下一個 C class 的 __init__，最後執行結果如下
# D.__init__
# C.__init__
# A.__init__

# 如果 super() 第二個參數為空，則回傳的 super 物件是 unbounded

class D(B, C):
    def __init__(self):
        
        print('super()')      
        print(super())      # <super: <class 'D'>, <D object>>
        print(super().__thisclass__)    # <class '__main__.D'>
        print(super().__self_class__)   # <class '__main__.D'>
        print(super().__self__)         # <__main__.D object at 0x0000020941AB8C10>   
        
        # 沒傳入參數時，class 都是 D，__self__ 為 D 物件
        
        print('super(D)')
        print(super(D))     # <super: <class 'D'>, NULL> 
        print(super(D).__thisclass__)    # <class '__main__.D'>
        print(super(D).__self_class__)   # None
        print(super(D).__self__)         # None

        # 傳入一個參數時，__self_class__ 與 __self__ 都是 None，所以 super(D) 為 unbounded 沒錯  
        
        print('super(D, D)')
        print(super(D, D))   # <super: <class 'D'>, <D object>>
        print(super(D, D).__thisclass__)    # <class '__main__.D'>
        print(super(D, D).__self_class__)   # <class '__main__.D'>
        print(super(D, D).__self__)         # <class '__main__.D'>
        
        # 傳入(D,D)時，連 __self__ 也是 <class '__main__.D'>
        
        print('super(D, self)')
        print(super(D,self))# <super: <class 'D'>, <D object>> 
        print(super(D, self).__thisclass__)    # <class '__main__.D'>
        print(super(D, self).__self_class__)   # <class '__main__.D'>
        print(super(D, self).__self__)         # <__main__.D object at 0x0000020941AB8C10>   
                
        print(super().__init__)      # <bound method B.__init__ of <__main__.D object at 0x000002A84945B340>>
        print(super(D).__init__())     # <method-wrapper '__init__' of super object at 0x000002A849463080>    
        print(super(D,D).__init__)   # <function B.__init__ at 0x000002A84944B400>  
        print(super(D,self).__init__)# <bound method B.__init__ of <__main__.D object at 0x000002A84945B340>>
        
    def funcX():
        pass
    
    def funcY(self):
        pass
        
d = D()


# 如果第二個參數是物件，則須滿足 isinstance(obj, type)

class D(B, C):
    def __init__(self):
        print('D.__init__')
        print(isinstance(self, B)) # True
        super(B, self).__init__()

# 如果第二個參數是 type，則須滿足 issubclass(type2, type)

# 額外說明 method-wrapper :
# method-wrapper 物件是 wrapping 一個 C 方法 

class Test:
        
    def method_one(self):
        print('method one')
        pass
    
    def method_two():
        print('method two')
        pass

# 額外說明 Bound Method :
# 如果一個 function 是 class 的 attribute，且可以透過 instance 存取，我們稱之為 bound method。
# 另外 bound method 的第一個參數為 self，bound method 也稱作 instance method。

try:    
    test = Test()
    test.method_one() # 會被轉成 Test.method_one(test)
    test.method_two() 
    # TypeError: Test.method_two() takes 0 positional arguments but 1 was given
except:
    pass

# 改法如下

class Test:
        
    def foo(self):
        print('foo from Test')
        pass    
        
    def method_one(self):
        print('method one')
        pass
    
    # 此 decorator 告訴 metaclass type 不要替 method_two 建立 bound method
    @staticmethod
    def method_two():
        print('method two')
        pass
        
test = Test()        
test.method_two() #method two

# 額外說明 Unbound Method :
# 第一個參數沒有 instance 的 method 稱為 unbound method，現在稱為 function
# Python 3 以後移除了 unbound Method

# 假設我們現在有一個 class 如下

class C(object):
    def foo(self):
        print('foo')
        pass

try:
    print(C.foo) 
    # <function C.foo at 0x0000021B4272BB50> 
    # Python 2.0 以前的說法這是一個 unbound method    
except:
    pass

c = C()
t = Test()
    
print(C.__dict__['foo']) # <function C.foo at 0x000002315B42BA30>
print(C.__dict__['foo'].__get__(None, C))   # <function C.foo at ...>
print(C.__dict__['foo'].__get__(None, c))   # <function C.foo at ...>
print(C.__dict__['foo'].__get__(None, Test))# <function C.foo at ...>
print(C.__dict__['foo'].__get__(None, t))   # <function C.foo at ...>

print(C.__dict__['foo'].__get__(c))         # <bound method C.foo of <__main__.C object at ...>>
print(C.__dict__['foo'].__get__(c, None))   # <bound method C.foo of <__main__.C object at ...>>
print(C.__dict__['foo'].__get__(c, C))      # <bound method C.foo of <__main__.C object at ...>>
print(C.__dict__['foo'].__get__(c, Test))   # <bound method C.foo of <__main__.C object at ...>>
print(C.__dict__['foo'].__get__(c, t))      # <bound method C.foo of <__main__.C object at ...>>
print(C.__dict__['foo'].__get__(t, t))      # <bound method C.foo of <__main__.Test object at ...>>
print(C.__dict__['foo'].__get__(t, Test))   # <bound method C.foo of <__main__.Test object at ...>>
print(C.__dict__['foo'].__get__(Test, t))   # <bound method C.foo of <class '__main__.Test'>>
print(C.__dict__['foo'].__get__(Test, Test))# <bound method C.foo of <class '__main__.Test'>>
print(C.__dict__['foo'].__get__(C))         # <bound method C.foo of <class '__main__.C'>>

C.__dict__['foo'].__get__(c)()         # foo
C.__dict__['foo'].__get__(c, None)()   # foo
C.__dict__['foo'].__get__(c, C)()      # foo
C.__dict__['foo'].__get__(c, Test)()   # foo
C.__dict__['foo'].__get__(c, t)()      # foo
C.__dict__['foo'].__get__(t, t)()      # foo
C.__dict__['foo'].__get__(t, Test)()   # foo
C.__dict__['foo'].__get__(Test, t)()   # foo
C.__dict__['foo'].__get__(Test, Test)()# foo

# function 因為有 __get__ 所以是 descriptor
# 注意上面我們分別傳入類別與物件

# 如果我們不要 class 的方法變成 method，可以使用 @staticmethod 修飾

class Honda:

    mileage = 10
    crok = [4,5]
    
    def __init__(self, ):        
        pass
        
    def __set__(self, source):
        print(id(source))
        print(locals())
        source.append(6)
        
    def __get__(self):
        return mileage

print(dir(Honda))
        
accourd = Honda()
newCount = 30
list = [1,2,5]
print(id(list))
accourd.__set__(list)

print(list)

'''

class C(object):
    @staticmethod
    def foo():
        print('static foo')
        pass

# 等同       
        
class C(object):
    
    def foo():
        print('static foo')
        pass

    foo = staticmethod(foo)
    
# 模擬 StaticMethod

class StaticMethod:
    "Emulate PyStaticMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        print('StaticMethod init')
        self.f = f

    def __get__(self, obj, objtype=None):
        print('static get')
        return self.f

    def __call__(self, *args, **kwds):
        return self.f(*args, **kwds)
        
# 使用 StaticMethod 模擬 @staticmethod       
        
class C(object):
    
    def foo():
        print('static foo')
        pass

    foo = StaticMethod(foo) 

# StaticMethod init
    
print(C.foo)                            # <function C.foo at 0x000001642408BAC0>
# static get                         
print(C.__dict__['foo'])                # <staticmethod(<function C.foo at 0x000001BA6B39BB50>)> 
print(C.__dict__['foo'].__get__(D))     # <function C.foo at 0x000001642408BAC0>    
print(C.__dict__['foo'].__get__(C))     # <function C.foo at 0x000001642408BAC0>
print(C.__dict__['foo'].__get__(c))     # <function C.foo at 0x000001642408BAC0>

# C.foo 使用 dot operator 會呼叫 __get__()，所以回傳的是 function C.foo 
# C.__dict__['foo'] 透過 __dict__ 呼叫不像 dot operator 會觸發 __get__()，回傳的是 staticmethod 物件

print('')

class Car:
    
    def __get__(self, instance, owner):
        print('get')
        print('self = ', self)
        print('instance =', instance)
        print('owner =', owner)
        return self.model
        
    def __set__(self, instance, value):
        self.model = value
        
class Honda:

    car = Car()
    
    def __init__(self):        
        pass
        
s = Honda();
s.car = 'Scion'
s.car
# get
# self =  <__main__.Car object at 0x000001F3D12986D0>
# instance = <__main__.Honda object at 0x000001F3D1298640>
# owner = <class '__main__.Honda'>


# 只要是有以下方法的'物件'就是 'descriptor'
# __get__ non-data descriptor method, for example on a method/function
# __set__ for example on a property instance or slot
# __delete for example on a property instance or slot
# 這三個也是俗稱的 'descriptor methods'

# '只'定義 __set__ 的 稱為 data descriptor
# 有定義 __set__, __delete__ 也稱為 data descriptor

# 這些 descriptor 物件在其他的 class 中是 'attribute'
# 換句話說，他們活在 class object 的 __dict__ 中

# function/method, bound method, property, classmethod, staticmethod 都是 descriptor，都使用上述的 'special method' 

# data descriptor 像是 property，可以允許 lazy evaluation

# 另外一個 data descriptor，像是 __slot__ 建立的 member_descriptor，有 memory saving 與 faster lookup 的功效，class 藉由將資料存在 mutable tupe-like 的資料結構，而不是較彈性但較占空間的 __dict__

# Non-data descriptor 像是 instance method / class method，implicitly 取得第一個參數(通常是 self 或是 cls) 透過 Non-data descriptor method __get__，這也是 static method 知道不有 implicit first argument 的原因。

print(classmethod.__get__) # 只有 __get__
# print(classmethod.__set__)
# print(classmethod.__delete__)
print(staticmethod.__get__) # 只有 __get__
# print(staticmethod.__set__)
# print(staticmethod.__delete__)

class Ten:
    def __get__(self, obj, objtype=None):
        return 10

class C(object):
    
    x = 5
    ten = Ten()
    
    def foo(self):
        print('foo')
        pass
        
c = C()

print(C.__dict__)

print(c.__dict__)

'''
