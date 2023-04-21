from pprint import pprint


# 如果 function 修改參數傳入的物件，caller 會看到變更如下

class Honda:
    
    city = ['Boston', 'NYC', 'Terrance']
    
    def __init__(self):
        print('')
        print('Honda init locals', locals())
        print('')
        pass
        
    def add(self, passengers2, city):
        
        
        passengers2.append('Calro')
        city = self.city
        print('id(passengers) after append', id(passengers2))
        print('id(city) after assign', id(city))
        
    def __get__(self):
        return mileage
        
car = Honda()
passengers = ['Mike', 'Garron', 'Errin']
city = ['Dallas', 'Takoma', 'Brown']

print('id(passengers)', id(passengers))
print('id(city)', id(city))

car.add(passengers, city)

print(passengers)
print(city)

# id(passengers) 2571706055488
# id(city) 2571706367040
# id(passengers) after append 2571706055488
# id(city) after assign 2571706121856
# ['Mike', 'Garron', 'Errin', 'Calro']
# ['Dallas', 'Takoma', 'Brown']

# 在函式中 append 會看到，原先傳入的 passengers 被修改了多了一個 'Calro'
# 但是如果是用 assign 的方式，則不會修改到傳入的物件 city

# namespace 是從 name 到 object 的對應。大部分的 namespace 現在都是以 Python 的 dictionary 被實作。
# namespace 的例子有：built-in names 的 set（包含如 abs() 的函式，和內建的 exception name）
# 模組中的全域 (global) name
# 和在函式調用中的區域 (local) name

import mod1
# # mod1 如下
# name = 'John'
# age = 20
# 
# def run():
# 	print(globals())

player1 = 'Jordan'
print(' ')
print(' ')
def func():

    print('func locals()', locals())
    print('func globals()', globals())  
    pass

func()

class Foo:
    
    var = 10    

foo = Foo()
bar = Foo()
print('foo.__dict__=', foo.__dict__) # foo.__dict__= {}

foo.var = 100
print('foo.var=', foo.var)  # foo.var= 100
print('foo.__dict__=', foo.__dict__) # foo.__dict__= {'var': 100}
# instance dict 加入變數 var = 100

print('bar.var=', bar.var) # bar.var= 10
print('bar.__dict__=', bar.__dict__) # bar.__dict__= {}
# bar.var 因為 instance dict 沒有，所以找到 class dict 的 var

Foo.var = 60
print('foo.var=', foo.var)  # foo.var= 100
# 雖然 class 的 var 變了，但 foo 的 instance dict 還是有 var (100)
print('foo.__class__.var=', foo.__class__.var) # foo.__class__.var= 60
print('bar.var=', bar.var)  # bar.var= 60

# 在建立 instance 後，我們可以使用 dot notation 存取 class 的 attribute，就像我們在此處使用 obj.attr 所做的那樣。class attribute 是特定於 class object，但我們可以從 class 的任何 instance 存取它們。值得注意的是，class attribute 對 class 的所有 instance 都是通用的。如果我們修改 class attribute，則更改將在該 class 的所有 instance 中可見。

# 注意：把點表示法想像成我們在告訴 Python：“在 obj 中查找名為 attr 的屬性。如果我們找到了，就把它還給我。”

# 每當我們呼叫用一個 class 時，我們就是在建立該 class 的一個新的 instance。 instance 有自己的 .__dict__ 屬性，該屬性保存 instance 的 local scope 或 namespace 中的 name。這些 names 通常稱為 instance attributes，每個 instance 有自己的 instance attributes。這表示著如果我們修改 instance attribute，則更改將只對該 instance 有效。

# 要從 class 內部建立、更新或存取任何 instance attribute，我們需要使用 self 和 dot notation。這裡，self 是一個特殊的 attribute，表示當前 instance。另一方面，要從 class 外部更新或存取任何 instance attribute，我們需要建立一個 instance，然後使用點表示法。這是它的工作原理：


# set 是沒有重複元素的無序集合。大括弧或 set() 函數可用於建立 set。注意：要創建一個空集，你必須使用 set()，而不是 {}，{} 會建立一個空的 dict

class Node:

    def __init__(self, val):
        self.val = val
		
node = Node(10)
node2 = node
node3 = Node(10)

print(node is node3) # True
print(node is not node2) # False

print(id(node))
print(id(node2))


var1 = 20
var2 = 20

print(id(var1))
print(id(var2))

print(var1 is var2) # True

#not, and, or 的優先序是低於一般運算子(+-*/)，3者之間的優先序為 not > end > or，所以 A and not B or C 等同於 (A and (not B)) or C
# and 與 or 是所謂的 short-circuit 運算子，以 A and B and C 為例，假設 A 與 C 為 True，因為 A and B 為 False，所以 C 不會評估

# 將比較的結果或是其他 boolean expression 指派到變數

string1, string2, string3 = ('', 'Trondheim', 'Hammer Dance')
non_null = string1 or string2 or string3
non_null # 'Trondheim'
print(non_null)


sum = 20 + (3+4*2) - 9
# 假設我們想要取得 3+4*2 的值，則我們可以使用 :=
sum = 20 + (mid := 3+4*2) - 9 

print(sum) # 22
print(mid) # 11


assert (1, 2, 3)              < (1, 2, 4)
assert [1, 2, 3]              < [1, 2, 4]
assert 'ABC' < 'C' < 'Pascal' < 'Python'
assert (1, 2, 3, 4)           < (1, 2, 4) 
assert (1, 2)                 < (1, 2, -1) 
assert (1, 2, 3)             == (1.0, 2.0, 3.0)
assert (1, 2, ('aa', 'ab'))   > (1, 2, ('abc', 'a'), 4)

