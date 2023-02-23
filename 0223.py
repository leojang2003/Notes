https://stackoverflow.com/questions/114214/class-method-differences-in-python-bound-unbound-and-static
https://stackoverflow.com/questions/30190185/how-to-use-super-with-one-argument
https://stackoverflow.com/questions/35998998/what-is-wrapped-by-a-python-method-wrapper
https://stackoverflow.com/questions/10401935/python-method-wrapper-type
https://stackoverflow.com/questions/10401935/python-method-wrapper-type
https://stackoverflow.com/questions/13126727/how-is-super-in-python-3-implemented
https://stackoverflow.com/questions/22403897/what-does-it-mean-by-the-super-object-returned-is-unbound-in-python
https://www.artima.com/weblogs/viewpost.jsp?thread=236278
https://stackoverflow.com/questions/5033903/python-super-method-and-calling-alternatives
https://stackoverflow.com/questions/27954695/what-is-a-sibling-class-in-python
https://docs.python.org/3/reference/datamodel.html#customizing-class-creation
https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
https://www.honeybadger.io/blog/python-instantiation-metaclass/
https://towardsdatascience.com/python-variable-assignment-9f43aed91bff
https://towardsdatascience.com/python-variable-assignment-9f43aed91bff
https://stackoverflow.com/questions/1680528/how-to-avoid-having-class-data-shared-among-instances


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
        A.__init__(self) 
        # 沒有呼叫 super() 直接呼叫 A.__init__()
        
class C(A):
    def __init__(self):
        print('C.__init__')
        super(C, self).__init__()
   
class D(B, C):
    def __init__(self):
        print('D.__init__')
        super(D, self).__init__()

print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# MRO : D > B > C > A
        
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

print(D.__mro__)
d = D()
# (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# D.__init__
# C.__init__
# B.__init__
# A.__init__

# 如果我們調整 class D 的繼承順序，改成 C、B，則 MRO 變成 D > C > B > A，剛好沒問題。為了避免一開始的情況，class B 要改成呼叫 super().__init__() 如下

class A:
    def __init__(self):
        print('A.__init__')
        super(A, self).__init__()
        
class B(A):
    def __init__(self):
        print('B.__init__')        
        super(B, self).__init__()
        # 沒有呼叫 super() 直接呼叫 A.__init__()
        
class C(A):
    def __init__(self):
        print('C.__init__')
        super(C, self).__init__()
   
class D(B, C):
    def __init__(self):
        print('D.__init__')
        super(D, self).__init__()

print(D.__mro__)
d = D()

# super() 的 signature 如下
# class super(type, object_or_type=None)
# super()回傳一個 proxy object 委派 method call 給 type 的 parent 或 sibling class
# object_or_type 決定 MRO 找尋的順序，會從 object_or_type 下一個 class 開始

class A:
    def __init__(self):
        print('A.__init__')
        super(A, self).__init__()
        
class B(A):
    def __init__(self):
        print('B.__init__')        
        super(B, self).__init__()
        # 沒有呼叫 super() 直接呼叫 A.__init__()
        
class C(A):
    def __init__(self):
        print('C.__init__')
        super(C, self).__init__()
   
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

# 如果 super() 第二個參數為空，則回傳的 super 物件是 unbounded ?!

class D(B, C):
    def __init__(self):        
        print(super())      # <super: <class 'D'>, <D object>>
        print(super(D))     # <super: <class 'D'>, NULL> 
        print(super(D,D))   # <super: <class 'D'>, <D object>>
        print(super(D,self))# <super: <class 'D'>, <D object>> 
        
        print(super().__init__)      # <bound method B.__init__ of <__main__.D object at 0x000002A84945B340>>
        print(super(D).__init__)     # <method-wrapper '__init__' of super object at 0x000002A849463080>    
        print(super(D,D).__init__)   # <function B.__init__ at 0x000002A84944B400>  
        print(super(D,self).__init__)# <bound method B.__init__ of <__main__.D object at 0x000002A84945B340>>
        
        # super(D,self).__init__()
        print(super(D).__init__())
        print('end')
    
    def funcX():
        pass
    
    def funcY(self):
        pass
        
d = D()

# print('d.__get__', d.__ge__())

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
# 第一個參數沒有 instance 的 method 稱為 unbound method
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
    
print(C.__dict__['foo']) # <function C.foo at 0x000002315B42BA30>
print(C.__dict__['foo'].__get__(C)) # <bound method C.foo of <class '__main__.C'>>   
print(C.__dict__['foo'].__get__(None, C)) # <function C.foo at 0x0000022C2F95BA30>  
print(C.__dict__['foo'].__get__())

# object.__get__(self, instance, owner=None)
# 取得 owner class 的 attribute (class attribute access) 或是該 class 的 instance 
# (instance attribute access)   
    
