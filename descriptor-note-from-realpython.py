# 有定義 __set__ ( __delete__ 為 optional) 的 稱為 data descriptor
# 只有有定義 __get__, 稱為 non-data descriptor

# dot operator 的存取順序為

# 1. data descriptor 的 __get__
# 2. object 的 __dict__
# 3. non-data descriptor 的 __get__
# 4. object type 的 __dict__
# 5. 依照 MRO 依上面順序 1~4 走一遍父類別
# 6. 拋出 AttributeError

# 因此 data 與 non-data descriptor 在 lookup 時是有順序的差異的

# 基本 descriptor protocol 如下

def __get__(self, obj, type=None) -> object:
    pass
def __set__(self, obj, value) -> None:
    pass

# self 為 descriptor 的 instance
# obj 為 descriptor instance 所在的 object
# type 為 descriptor instance 所在的 object 的 type
# __set__() 沒有 type 變數，因為 __set__() 只能從物件呼叫，但 __get__() 可同時由 object 或 class 呼叫

# ☆☆☆☆
# 另外重要的一點是，Python descriptors 在每個 class 指初始化一次，每個 class 的 instance 的 descriptor 都是同一個 instance

# descriptors2.py
class OneDigitNumericValue():
    def __init__(self):
        self.value = 0
    def __get__(self, obj, type=None) -> object:
        return self.value
    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value = value

class Foo():
    number = OneDigitNumericValue()

my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number) # 3
print(my_second_foo_object.number) # 3 

my_third_foo_object = Foo()
print(my_third_foo_object.number) # 3

# __set_name__(self, owner, name)
# Python 3.6 之後，每當我們 instantiate 一個 descriptor 時，會自動呼叫此 method 並自動設定 name 屬性

# descriptors5.py
class OneDigitNumericValue():
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value

class Foo():
    number = OneDigitNumericValue()

my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)
print(my_second_foo_object.number)

my_third_foo_object = Foo()
print(my_third_foo_object.number)

# 以下為利用 non-data descriptor 的 lookup 順序低於 obj.__dict__ 的特性
# 利用 obj.__dict__ 當 cache 而不需要再呼叫耗時的 meaning_of_life()

import time

class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]

class DeepThought:
    @LazyProperty
    def meaning_of_life(self):
        print('I\'m thinking')
        time.sleep(3)
        return 42

deep = DeepThought()
print(deep.meaning_of_life) # I'm thinking 
print(deep.meaning_of_life) # obj.__dict__['meaning_of_life'] 即刻回傳，沒有執行 meaning_of_life()
print(deep.meaning_of_life) # 同上

#
