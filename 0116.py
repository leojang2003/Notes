import os
import logging
import collections



#
# 介紹 metaclass
#    
class Philosopher:
    def __init_subclass__(cls,/,default_name, **kwargs):            
        super().__init_subclass__(**kwargs)
        cls.default_name = default_name
        
class AsianPhilosopher(Philosopher, default_name= 'Leo'):
    
    def __init_subclass__(cls,/,default_name, **kwargs):            
        print('__init_subclass__')
    
    def __set_name__(self, owner, x):
        print(x)
    pass
    
tim = AsianPhilosopher()
print('AsianPhilosopher', tim)
print(AsianPhilosopher.__bases__) #(<class '__main__.Philosopher'>,)
print(tim.__class__) #<class '__main__.AsianPhilosopher'>

# type() 是用來找物件的 type 或是 class，回傳該物件的 type 或是 class
print(type(tim)) #<class '__main__.AsianPhilosopher'>

print(type(AsianPhilosopher)) #<class 'type'>
# 據我們觀察，即所有的 class 都是 class 'type' 的物件(注意是物件)。此 type 為一個 class 與 type() function 不同。'type' class 在 Python 裡叫做 Metaclass。

print(type(int)) #<class 'type'>
print(type(type(AsianPhilosopher.__set_name__))) #<class 'type'>
print(type(float)) #<class 'type'>
print(type(object)) #<class 'type'>
# 甚至連 'object' class 都是 type
# type class 是 int, float class，同時也是 built-in object class 的 metaclass
# 是所有 Python class 的 base class

print(type(type)) #<class 'type'>
# type 的 metaclass 是自己

# 重點
# metaclass 是平常較少用到的概念，但與物件的生成有關係，所以先做介紹
# 講到這有兩個重點
# 1. 所有的 class 在 Python 都是 'type' class 的物件，此 type class 為 Metaclass。
# 2. 每個 class 都預設繼承 'object' base class

class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
human_object = Human("Virat", "Kohli")
print(isinstance(human_object, Human)) #True

# 仔細觀察 Human，__init__ 並沒有回傳任何東西，為什麼呼叫 Human class 會回傳 human_object?
# 另一個問題是 __init__ 怎麼取得 self 的?

# 物件的建立有兩個步驟，步驟一是物件的建立，步驟二是物件初始化。通常我們感興趣的是步驟二。Python 使用 __new__ 在步驟一，使用 __init__ 在步驟二。

# 如果 class 沒有定義這些 method，則它們是從 'object' base class 繼承的。由於 Human class 沒有定義 __new__ 方法，所以在 oject initialization 的過程中，會 呼叫 'object' class 的__new__方法，而初始化時會呼叫 Human class 的__init__方法。接下來，我們將詳細介紹這些方法中的每一種。

#
# __new__() 方法
#

# __new__ 方法是 object initialization 過程的第一步。它是 'object' class的靜態方法(static method)，接受 cls 或 class reference 作為第一個參數。其餘參數（Virat 和 Kohli）在呼叫 Human("Virat", "Kohli") 時傳遞。 __new__ 方法創建一個 cls class 的 instance（也就是說，它通過使用 super().__new__(cls) 呼叫父類別 'object' class 的 __new__ 方法，配置記憶體給此物件）。然後它回傳 cls type 的 instance。

# 通常，它不進行任何初始化，因為這是 __init__ 方法的工作。但是，當我們覆寫 __new__ 方法時，我們可以使用它來初始化 object 或在回傳物件前根據需要修改它。

# __new__ 的 signature如下
# cls - 必要參數。__new__ method 回傳的物件為 cls type
# @staticmethod
# def __new__(cls[,...]):
    # pass

# 考慮以下範例

class Human:
    def __new__(cls, first_name=None):
        # cls = Human. cls 為用來建立物件的類別
        print('cls', cls) # <class '__main__.Human'>
        # 建立的物件會是 type cls
        # 我們必須呼叫 object class 的 __new__ 來配置記憶體
        obj = super().__new__(cls) # 等同 object.__new__(cls)
        

        # 修改產生的 object
        if first_name:
            obj.name = first_name
        else:
            obj.name = "Virat"

        print(obj) # <__main__.Human object at 0x000002783C14D000>
        # 回傳物件
        return obj

# 建立物件
# 會呼叫 `object` class 的 __init__ method
virat = Human()
print(virat) #<__main__.Human object at 0x0000021A7669D060>

print(virat.name)  # Virat

sachin = Human("Sachin")
print(sachin.name)  # Sachin

# 上述的 __new__ 被改寫，注意 __new__ 雖然是 object class 的 static method，但我們覆寫的時候不需要加上 @staticmethod 修飾子

# 在 Human class 的 __new__ 方法中，我們首先使用 super().__new__(cls) 呼叫 'object' class 的 __new__ 方法。'object' class 類的 __new__ 方法建立並回傳 class 的 instance，class 是當成參數傳給 __new__ 方法。在這裡，當我們傳遞 cls（即 Human class reference）時；該對象的 __new__ 方法將返回一個 Human type 的 instance。

# 我們必須在覆寫的 __new__ 方法中呼叫 'object' class 的 __new__ 方法來建立物件並為物件配置記憶體。

# Human class 的 __new__ 方法修改 'object' calss 的 __new__ 方法回傳的 obj 並為其新增 name 屬性。因此，使用 Human class 建立的的所有 object 都將具有 name 屬性。因此我們修改了 Human class 的 object initialization 過程。

# 讓我們考慮另一個例子。在此範例中，我們正在建立一個名為 Animal 的新 class 並覆蓋 __new__ 方法。在這裡，當我們從 Animal 類的 __new__ 方法呼叫 'object' class 的 __new__ 方法時，我們不是將 Animal 的 class reference 作為參數傳遞給 'object' class 的 __new__ 方法，而是傳入 Human 的 class reference。因此，從 'object' class 的 __new__ 方法回傳的 object 將是 Human type 而不是 Animal type。結果，呼叫 Animal class（即 Animal()）回傳的 object 將是 Human type。

class Animal:
    def __new__(cls):
        # 傳入 Human class reference 而不是 Animal class reference
        obj = super().__new__(Human) # 等同 object.__new__(Human)

        print(f"Type of obj: {type(obj)}") # Type of obj: <class '__main__.Human'>

        # 回傳物件
        return obj

# 建立物件
cat = Animal()
# Output:
# Type of obj: <class '__main__.Human'>

type(cat)   # Output: <class '__main__.Human'>

#
# __init__() 方法
# 

# __init__ 方法是 Python 中 object initialization 過程的第二步。它的第一個參數作使用 __new__ 方法回傳的 object 或 instance。其餘參數是呼叫類別 (Human("Virat", "Kohli")) 時傳遞的參數。這些參數用於初始化物件。 __init__ 方法不得回傳任何內容。如果您嘗試使用 __init__ 方法回傳任何內容將引發異常，如下所示：

class Human:
    def __init__(self, first_name):
        self.first_name = first_name
        return self

try:       
    human_obj = Human('Virat') 
    # __init__() should return None, not 'Human'
except:
    pass

# 補充說明 super():

class A1:
    def __new__(cls, *args, **kwargs):
        print('A1 cls', cls)
        obj = super().__new__(cls)    
        obj.A1 = True
        return obj
class A2(A1):
    def __new__(cls, *args, **kwargs):
        print('A2 cls', cls)
        obj = super().__new__(cls)
        obj.A2 = True;
        return obj
class A3(A2):
    def __new__(cls, *args, **kwargs):
        print('A3 cls', cls)        
        human_obj = super().__new__(cls)    
        human_obj.A3 = True;
        return 
class A4(A3):
    def __new__(cls, *args, **kwargs):
        print('A4 cls', cls)
        obj = super(A3, cls).__new__(cls)
        return obj
    pass

# 首先 class.__mro__ 顯示尋找 base classes 在 method resolution 
print(A4.__mro__)
# (<class '__main__.A4'>, <class '__main__.A3'>, <class '__main__.A2'>, <class '__main__.A1'>, <class 'object'>)

a4 = A4()
print(a4.A1)

#
# super()深度解釋
#
class LogginDict(dict):
    def __setitem__(self, key, value):
        logging.info('Setting %r to %r' % (key, value))
        super().__setitem__(key, value)

itm = LogginDict()
itm.__setitem__('e', 'e2')
print(itm['e']) # e2
# 我們這裡建立一個類別繼承 dict 類別，使用 super() 呼叫 dict 的 __setitem__，在super()以前，必須使用 dict.__setitem__(self, key, value)。super()是一個 computed 'indirect' reference。如果我們將繼承的類別換成其他的類別時，super()可以自動指向其 base class

# class SomeOtherMapping:
    # pass

# class LogginDict(SomeOtherMapping): # 新的 base class
    # def __setitem__(self, key, value):
        # logging.info('Setting %r to %r' % (key, value))
        # super().__setitem__(key, value) # 不需要變更

# 動態生成 indirection ...
# 與呼叫 super 所在的 class 與 on the instance's tree ancestor 有關(?!)

class LoggingOD(LogginDict, collections.OrderedDict):
    pass
    

print(LoggingOD.__mro__)
# 現在這個新類別的 ancestor tree 是
# (
    # <class '__main__.LoggingOD'>, 
    # <class '__main__.LogginDict'>,  
    # <class 'collections.OrderedDict'>, 
    # <class 'dict'>, 
    # <class 'object'>
# )

# 注意 OrderedDict 在 LogginDict 與 dict 之間，這表示現在 LogginDict.__setitem__ 現在會分派給 OrderedDict 而不是 dict 去做 key/value 更新

# LoggingOD 在 LogginDict、OrderedDict 之前
# LogginDict 在 OrderedDict 之前因為 LogginOD.__bases__為(LogginDict、OrderedDict)
# LogginDict 在 dict 之前
# OrderedDict 在 dict 之前
# dict 在 object 之前

# 解決這些限制的過程叫做 linearization

# 要知道MRO是如何計算的。基礎很簡單。該序列包括 class ，它的 base calss，以及這些 base 的 base class 等等，直到到達 object ，它是所有 class 的 root class。序列是有序的，這樣一個 class 總是出現在它的 parent 之前，如果有多個 parent，它們與 base class 的 tupe 保持相同的順序。

# 我們只需要記住 1. 子類別在父類別之前 2. 需考量 __bases__ 中出現的順序

# super() 的用途就是委派方法呼叫(delagating method calls)到 instance 的 ancestor tree 中的某些 class。為了成功呼叫，須解決以下三個問題
# 1. super()呼叫的方法須存在
# 2. 呼叫者與被呼叫叫者須有相同的 argument signature
# 3. 每次方法都須使用 super()

# 我們程式在寫呼叫 super() 時，並不知道最後被呼叫的類別為何，因為之後才寫的 subclass 可能會引進新的類別到 MRO 中。第一種方法是大家使用 positional arguments，如同 __set_name__ 有固定兩個參數 key/value
# 叫彈性的作法是每個 ancestor 的 method 都接受 keyword argument 與 keyword-arguments dictionary，移除自己需要的參數，並轉傳**kwds(包含其他剩餘的參數)，在呼叫chain的最後時，dict為空
# 每一層都取自各自所需的 keyword arguments，最後空的 dict 會傳到不需要參數的 method (舉例來說，object.__init__ 就不需要參數)

class Shape:
    def __init__(self, shapenmae, **kwds):
        self.shapenmae = shapenmae
        super().__init__(**kwds)

class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)

cs = ColoredShape(color='red', shapenmae='Circle')
    
# 接下來是要確保 target method 存在    

# 上面的例子展示了最簡單的情況。我們知道 object 有一個 __init__ 方法，並且 object 始終是 MRO 鏈中的最後一個 class，因此任何對 super().__init__ 的一系列呼叫都保證最後以呼叫 object.__init__結束。換句話說，我們保證 super() 呼叫的目標保證存在，並且不會因 AttributeError 而失敗。

# 對於 'object' 所沒有的方法（例如 draw() 方法）的情況，我們需要編寫一個保證在 'object' 之前呼叫的 root class。root class 的職責只是吃掉 method call 而不使用 super() 將 call forward。

# Root.draw 還可以使用 assertion 進行防禦性編程，以確保它不會遮蔽鏈中稍後的其他 draw() 方法。如果子類錯誤地合併了一個具有 draw() 方法但未從 Root 繼承的類，則可能會發生這種情況：

# 情境一

class Root:
    def draw(self):
        # the delegation chain stops here
        assert not hasattr(super(), 'draw')

class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting shape to:', self.shapename)
        super().draw()

class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super().draw()

cs = ColoredShape(color='blue', shapename='square')
cs.draw()

# 情境二

class Root():
    def draw(self):            
        assert not hasattr(super(), 'draw')
        pass

# 不繼承自 Root class    
class Glitch:
    
    def __new__(cls, *args, **kwargs):                       
        return super().__new__(cls)

    # 有 draw 方法
    def draw(self):
        print('Glitch draw')
        pass

class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting shape to:', self.shapename)
        super().draw()

class ColoredShape(Shape, Glitch):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super().draw()
        
print(ColoredShape.__mro__)
# (<class '__main__.ColoredShape'>, <class '__main__.Shape'>, <class '__main__.Root'>, <class '__main__.Glitch'>, <class 'object'>)，這裡在 MRO 中 Glitch 在 Root 之後，所以 Root 的 hasattr(super(), 'draw') 會是 True，進而拋出 AssertionError

cs = ColoredShape(color='blue', shapename='square')
cs.draw()

# 如果 subclasses 想要將其他 class 注入到 MRO 中，那些其他 class 也需要繼承 Root ，這樣呼叫 draw() 的路徑就無法在沒有被 Root.draw 停止的情況下到達 object。這應該清楚地記錄下來，以便編寫新的協作 class 的人知道從 Root 繼承。這個限制與 Python 自己要求所有新的異常都必須繼承自 BaseException 類似。

# 上面顯示的技巧確保 super() 呼叫已知存在的方法並且 signature 將是正確的；然而，我們仍然依賴於在每一步呼叫 super() 以便委託鏈繼續不間斷。如果我們合作設計類，這很容易實現——只需向鏈中的每個方法添加一個 super() 呼叫。

# 上面列出的三種技巧提供了設計可由子類組合或重新排序的協作類的方法。

***************

如何合併非合作班級

有時，子類可能希望與不是為它設計的第三方類一起使用協作多重繼承技術（可能它感興趣的方法不使用 super() 或者該類可能不從根類繼承).通過創建一個遵守規則的適配器類可以很容易地解決這種情況。

例如，下面的 Moveable 類不進行 super() 調用，它有一個與 object.__init__ 不兼容的 __init__() 簽名，並且它不繼承自 Root：

class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print('Drawing at position:', self.x, self.y)
If we want to use this class with our cooperatively designed ColoredShape hierarchy, we need to make an adapter with the requisite super() calls:

class MoveableAdapter(Root):
    def __init__(self, x, y, **kwds):
        self.movable = Moveable(x, y)
        super().__init__(**kwds)
    def draw(self):
        self.movable.draw()
        super().draw()

class MovableColoredShape(ColoredShape, MoveableAdapter):
    pass

MovableColoredShape(color='red', shapename='triangle',
                    x=10, y=20).draw()
    
    
# 建立一個同時有 __new__ 與 __init__ 的類別如下
    
class Human:
    def __new__(cls, *args, **kwargs):
        # 這裡，object class 的 __new__ method 必須被呼叫以建立物件並配置物件的記憶體
        print("Inside new method")
        print(f"args arguments {args}")
        print(f"kwargs arguments {kwargs}")
        
        human_obj = super(Human, cls).__new__(cls)

        print(f"human_obj instance - {human_obj}")
        return human_obj

    # 因為我們覆寫了 __init__ method, 所以 object class 的 __init__ method 不會被呼叫
    def __init__(self, first_name, last_name):
        print("Inside __init__ method")
        # self = human_obj returned from the __new__ method

        self.first_name = first_name
        self.last_name = last_name

        print(f"human_obj instance inside __init__ {self}: {self.first_name}, {self.last_name}")

human_obj = Human("Virat", "Kohli")

# Output
# Inside new method
# args arguments ('Virat', 'Kohli')
# kwargs arguments {}
# human_obj instance - <__main__.Human object at 0x103376630>
# Inside __init__ method
# human_obj instance inside __init__ <__main__.Human object at 0x103376630>: Virat, Kohli

# 在上面的代碼中，我們覆蓋了對像類的 __new__ 和 __init__ 方法。 __new__ 創建 Human 類類型的對象 (human_obj) 並返回它。一旦 __new__ 方法完成，Python 就會調用 __init__ 方法，並將 human_obj 對像作為第一個參數。 __init__ 方法初始化 human_obj，名字為 Virat，姓氏為 Kohli。由於對象創建是第一步，初始化是第二步，所以 __new__ 方法總是在 __init__ 方法之前被調用

# __init__ 和 __new__ 在 Python 中都被稱為魔術方法。魔術方法的名稱以 __（雙下劃線或“dunder”）開頭和結尾。魔術方法由 Python 隱式調用；您不必明確地調用它們。例如，__new__ 和 __init__ 方法都被 Python 隱式調用。讓我們再介紹一個神奇的方法，__call__。

__call__ 方法
__call__ 方法是 Python 中的一個神奇方法，用於使對象可調用。可調用對像是可以調用的對象。例如，函數是可調用對象，因為它們可以使用圓括號調用。

考慮一個示例以更好地理解可調用對象：

def print_function():
    print("I am a callable object")

# print_function is callable as it can be called using round parentheses
print_function()

# Output
# I am a callable object
Let's try to call an integer object. As integer objects are not callable, calling them will raise an exception.

a = 10

# As the integer object is not callable, calling `a` using round parentheses will raise an exception.
a()   # Output: TypeError: 'int' object is not callable

可調用（）
可調用函數用於確定對像是否可調用。 callable 函數將對象引用作為參數，如果對像看起來是可調用的，則返回 True，如果對像不可調用，則返回 False。如果可調用函數返回 True，則該對象可能不可調用；但是，如果它返回 False，則該對象肯定不可調用。

# Functions are callable
callable(print_function)
# Output: True

# Interger object is not callable
callable(a)
# Output: False
Let's determine whether the classes in Python are callable. Here, we will determine whether the Human class defined earlier is callable.

callable(Human)
# Output: True
Yes, classes in Python are callable, and they should be! Don't you think so? When we call the class, it returns the instance of that class. Let's find out whether the objects created from the class are callable.

human_obj = Human("Virat", "Kohli")

callable(human_obj)   # Output: False

# Let's try calling the human_obj
human_obj()

# As human_obj is not callable it raises an exception
# Output: TypeError: 'Human' object is not callable

因此，human_obj 不可通過 human_obj 的類調用（即 Human 類是可調用的）。

為了使 Python 中的任何對像都可調用，Python 提供了 __call__ 方法，該方法需要由對象的類實現。例如，要使 human_obj 對象可調用，Human 類必須實現 __call__ 方法。一旦 Human 類實現了 __call__ 方法，就可以像函數一樣調用 Human 類的所有對象（即，使用圓括號）。

class Human:
    def __init__(self, first_name, last_name):
        print("I am inside __init__ method")
        self.first_name = first_name
        self.last_name = last_name

    def __call__(cls):
        print("I am inside __call__ method")

human_obj = Human("Virat", "Kohli")
# Output: I am inside __init__ method

# Both human_obj() and human_obj.__call__() are equaivalent
human_obj()
# Output: I am inside __call__ method

human_obj.__call__()
# Output: I am inside __call__ method

callable(human_obj)
# Output: True

上面的代碼輸出表明，在Human類上實現了__call__方法後，human_obj就變成了一個可調用對象。我們可以使用圓括號調用 human_obj（即 human_obj()）。當我們使用 human_obj() 時，Python 在後台調用 Human 類的 __call__ 方法。因此，我們可以直接調用 human_obj 上的 __call__ 方法（​​即 human_obj.__call__()），而不是將 human_obj 調用為 human_obj()。 human_obj() 和 human_obj.__call__() 是等價的，它們是一回事。

對於所有可調用的對象，它們的類必須實現 __call__ 方法。

我們知道函數是一個可調用對象，所以它的類（即函數）必須實現 __call__ 方法。讓我們在前面定義的 print_function 上調用 __call__ 方法。

print_function.__call__() # 輸出：I am a callable object
在 Python 中，類也是一個可調用對象；因此，它是一個類的類（元類）（即，類型類必須定義一個調用方法）。因此，當我們調用 Human() 時，Python 會在後台調用類​​型類的 call 方法。

粗略地說，類型類上的 __call__ 方法如下所示。這僅用於解釋目的；我們將在本教程後面介紹 __call__ 方法的實際定義。

class type:
    def __call__():
        # Called when class is called i.e. Human()
        print("type's call method")
With an understanding of __call__ method and how calling the class calls the __call__ method of the type class, let's find out the answer to the following questions regarding the object initialization process:

誰調用了 __new__ 和 __init__ 方法？
誰將 self 對像傳遞給 __init__ 方法？
由於__init__方法是在__new__方法之後調用的，而__init__方法沒有返回任何東西，調用類如何返回對象（即調用Human類如何返回human_obj對象）？
考慮一個在 Python 中實例化對象的示例。

class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

human_obj = Human("Virat", "Kohli")

我們知道，當我們調用類（即 Human("Virat", "Kohli")）時，會調用類型類的 __call__ 方法。但是，類型類的 __call__ 方法的定義是什麼？當我們談論 CPython 時，類型類的 __call__ 方法定義是用 C 語言定義的。如果我們把它轉換成 Python 並簡化它，它看起來有點像這樣：

# type's __call__ method which gets called when Human class is called i.e. Human()
def __call__(cls, *args, **kwargs):
    # cls = Human class
    # args = ["Virat", "Kohli"]
    # Calling __new__ method of the Human class, as __new__ method is not defined
    # on Human, __new__ method of the object class is called
    human_obj = cls.__new__(*args, **kwargs)

    # After __new__ method returns the object, __init__ method will only be called if
    # 1. human_obj is not None
    # 2. human_obj is an instance of class Human
    # 3. __init__ method is defined on the Human class
    if human_obj is not None and isinstance(human_obj, cls) and hasattr(human_obj, '__init__'):
        # As __init__ is called on human_obj, self will be equal to human_obj in __init__ method
        human_obj.init(*args, **kwargs)

    return human_obj

讓我們理解上面的代碼；當我們在後台執行 Human("Virat", "Kohli") 時，Python 將調用類型類的 __call__ 方法，該方法的定義類似於上面的代碼片段。如上所示，類型類的 __call__ 方法接受 Human 類作為第一個參數（cls 是 Human 類），其餘參數在調用 Human 類時傳遞。類型類的 __call__ 方法將首先調用定義在 Human 類上的 __new__ 方法，如果有的話；否則，調用 Human 類父類的 __new__ 方法（​​即對象的 __new__ 方法）。 __new__ 方法將返回 human_obj。現在，類型類的 __call__ 方法將以 human_obj 作為第一個參數調用定義在 Human 類上的 __init__ 方法。 __init__ 將使用傳遞的參數初始化 human_obj，最後， __call__ 方法將返回 human_obj。

Python中的對象實例化過程

因此，在 Python 中創建和初始化對象時遵循以下步驟：

調用 Human 類 - Human()；這在內部調用類型類的 __call__ 方法（​​即 type.__call__(Human, "Virat", "Kohli")）。
type.__call__ 將首先調用定義在 Human 類上的 __new__ 方法。如果 Human 類上沒有定義 __new__ 方法，就會調用對像類的 __new__ 方法。
__new__ 方法將返回 Human 類型的對象，即 human_obj
現在，type.__call__ 將以 human_obj 作為第一個參數調用定義在 Human 類上的 __init__ 方法。這個 human_obj 將是 __init__ 方法中的 self 。
__init__ 方法將 human_obj 初始化為 first_name 作為 Virat，thelast_name 作為 Kohli。 __init__ 方法不會返回任何東西。
最後，type.__call__ 將返回 human_obj 對象。
根據 type.__call__ 定義，每當我們創建一個新對象時，總會調用 __new__ 方法，但調用 __init__ 方法取決於 __new__ 方法的輸出。只有當 __new__ 方法返回一個 Human 類或 Human 類的子類類型的對象時，才會調用 __init__ 方法。

讓我們了解一些案例。

情況 1：如果 __new__ 方法返回的對像是 Human 類型（即 __init__ 方法的類），則將調用 __init__ 方法。

class Human:
    def __new__(cls, *args, **kwargs):
        print(f"Creating the object with cls: {cls} and args: {args}")
        obj = super().__new__(cls)
        print(f"Object created with obj: {obj} and type: {type(obj)}")
        return obj

    def __init__(self, first_name, last_name):
        print(f"Started: __init__ method of Human class with self: {self}")
        self.first_name = first_name
        self.last_name = last_name
        print(f"Ended: __init__ method of Human class")

human_obj = Human("Virat", "Kohli")
Output:

# Creating the object with cls: <class '__main__.Human'> and args: ('Virat', 'Kohli')
# Object created with obj: <__main__.Human object at 0x102f6a4e0> and type: <class '__main__.Human'>
# Started: __init__ method of Human class with self: <__main__.Human object at 0x102f6a400>
# Ended: __init__ method of Human class with self: <__main__.Human object at 0x102f6a400>
Case 2: If the __new__ method does not return anything, then __init__ will not be called.

class Human:
    def __new__(cls, *args, **kwargs):
        print(f"Creating the object with cls: {cls} and args: {args}")
        obj = super().__new__(cls)
        print(f"Object created with obj: {obj} and type: {type(obj)}")
        print("Not returning object from __new__ method, hence __init__ method will not be called")

    def __init__(self, first_name, last_name):
        print(f"Started: __init__ method of Human class with self: {self}")
        self.first_name = first_name
        self.last_name = last_name
        print(f"Ended: __init__ method of Human class")

human_obj = Human("Virat", "Kohli")
Output:

# Creating the object with cls: <class '__main__.Human'> and args: ('Virat', 'Kohli')
# Object created with obj: <__main__.Human object at 0x102f6a5c0> and type: <class '__main__.Human'>
# Not returning object from __new__ method, hence __init__ method will not be called

上面代碼中，調用了Human類的__new__方法；因此，創建了 Human 類型的 obj（即，為 obj 分配了內存）。但是，由於 __new__ 方法沒有返回 human_obj，所以 __init__ 方法不會被調用。此外，human_obj 將沒有創建對象的引用，因為它不是從 __new__ 方法返回的。

print(human_obj). # Output: None
Case 3: The __new__ method returns an integer object.

class Human:
    def __new__(cls, *args, **kwargs):
        print(f"Creating the object with cls: {cls} and args: {args}")
        obj = super().__new__(cls)
        print(f"Object created with obj: {obj} and type: {type(obj)}")
        print("Not returning object from __new__ method, hence __init__ method will not be called")
        return 10

    def __init__(self, first_name, last_name):
        print(f"Started: __init__ method of Human class with self: {self}")
        self.first_name = first_name
        self.last_name = last_name
        print(f"Ended: __init__ method of Human class")

human_obj = Human("Virat", "Kohli")

上面代碼中，調用了Human類的__new__方法；因此，創建了 Human 類型的 obj（即，為 obj 分配了內存）。但是__new__方法返回的不是human_obj，而是一個值為10的整數，不是Human類型；因此，不會調用 __init__ 方法。此外，human_obj 不會有創建對象的引用，但它會引用一個整數值 10。

print(human_obj)
# Output: 10
In scenarios where the __new__ method does not return the instance of the class and we want to initialize the object, we have to call the __init__ method, explicity, inside the __new__ method, as shown below:

class Human:
    def __new__(cls, *args, **kwargs):
        print(f"Creating the object with cls: {cls} and args: {args}")
        obj = super().__new__(cls)
        print(f"Object created with obj: {obj} and type: {type(obj)}")
        print("Not returning object from __new__ method, hence __init__ method will not be called")
        obj.__init__(*args, **kwargs)
        return 10

    def __init__(self, first_name, last_name):
        print(f"Started: __init__ method of Human class with self: {self}")
        self.first_name = first_name
        self.last_name = last_name
        print(f"Ended: __init__ method of Human class")

human_obj = Human("Virat", "Kohli")
Output:

# Creating the object with cls: <class '__main__.Human'> and args: ('Virat', 'Kohli')
# Object created with obj: <__main__.Human object at 0x102f6a860> and type: <class '__main__.Human'>
# Not returning object from __new__ method, hence __init__ method will not be called
# Started: __init__ method of Human class with self: <__main__.Human object at 0x102f6a860>
# Ended: __init__ method of Human class
In the above case, the __new__ method returned an integer object; hence the human_obj value will be 10.

print(human_obj)
# Output: 10
Conclusion
In this article, we explored the __new__, __init__, and __call__ magic methods and discussed Metaclass in Python. In doing so, we have a better understanding of the object creation and initialization processes in Python.

'''
