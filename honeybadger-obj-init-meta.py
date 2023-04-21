from pprint import pprint

# Python3 的 object base class 

# 在 Python3 中，所有 class 都 implicitly 繼承自 object base class。object class 提供了一些常用的 method，如 __init__、__str__ 和 __new__，這些方法可以被 subclass 覆寫。考慮下面的程式，例如：

class Human:
  pass

# 在上面的程式中，Human class 沒有定義任何 attribute 或 method。但是預設 Human class 繼承 object base class，因此它具有 object base class 定義的所有 attribute 和 method。我們可以使用 dir() 檢查 Human class 繼承或定義的所有 attribute 和 method。

# dir() 回傳在任何 Python object 上定義的所有 attribute 和 method 的 list。

print(dir(Human))

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']


# dir() 顯示 Human class 有許多 method 與 attribute，都是從 object base class 繼承來的
# class 的 __bases__ property 包含該 class 繼承的所有 base class 的清單。

print(Human.__bases__)
# Output: (< class 'object'>,)

print(dir(object))

# Output:
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__get attribute __', '__gt__', '__hash__', '__init__', '__init_sub class __', '__le__',
'__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
'__sizeof__', '__str__', '__sub class hook__']

# 上面的輸出顯示 Human class 有 object 作為 base class。



# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
# ☆☆☆   isinstance()    ☆☆☆
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆

#
# isinstance(obj, class_or_tuple, /)
# Return whether an object is an instance of a class or of a subclass thereof.
# 
# A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
# check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
# or ...`` etc.
# 如果是 subclass，isinstance()也會回傳 True
#

assert isinstance(Human, object) == True 
assert issubclass(Human, object) == True

# 上面可以看到 Human 是 object 的 subclass，所以 isinstance() 也會回傳 True



   
# object base class 提供了 __init__ 和 __new__ 方法，用於建立和初始化 class 的 object。我們將在後半部分詳細討論 __init__ 和 __new__ 方法。

# Python 是一種物件導向的程式語言。Python 中的一切都是 object(或稱做 instance)。class 、function，甚至簡單的 data type，如 integer 和 float，在 Python 中也是某個 class 的 object。每個 object 都有一個初始化來源的 class。為了獲取 object 的 class 或 type，Python 為我們提供了在 object 本身上定義的 type function 和 __class__ attribute。



# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
# ☆☆☆    認識 type()    ☆☆☆
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆


# 讓我們藉助簡單的 data type(例如 int 和 float)來理解 type function。

a = 9
type(a)  # < class 'int'>

b = 9.0
type(b)  # < class 'float'>

# 與其他語言不同，在 Python 中，9 是一個 int class 的 object，它由變數 a 引用(it is referred by the variable a)。同樣地，9.0 是 class float 的 object，由變數 b 引用。

# type 用於找尋 object 的 type 或 class。它接受一個我們想要找出其 type 的 object 作為第一個參數，並回傳該 object 的 type 或 class。

# 我們還可以使用 object 的 __class__ property 來找尋 object 的 type 或 class。
# __class__ 是 object 上的一個 attribute，它參考到建立 object 的 class。

a.__class__  # < class 'int'>
b.__class__  # < class 'float'>

# 在簡單的 data type 之後，現在讓我們藉助使用者定義的 class Human 來了解 type function 和 __class__ attribute。

human_obj = Human()

print(type(human_obj))     # Output: < class '__main__.Human'>
print(human_obj.__class__) # Output: < class '__main__.Human'>

# 定義一個簡單的 function
def simple_function():
  pass

print(type(simple_function))     # Output: < class 'function'>
print(simple_function.__class__) # Output: < class 'function'>

print(type(Human))      # Output: < class 'type'>
print(Human.__class__)  # Output: < class 'type'>

assert issubclass(Human, type) == False
# Human 不是 type 的 subclass

assert isinstance(Human, type) == True
# Human 是 type 的 instance
# 所以我們知道 Python 的 class 是 type class 的 instance

customHuman = type('X', (), dict(a=1, b=2))
p1 = Human()
p2 = customHuman()
print(p1) # <__main__.Human object at ...>
print(p2) # <__main__.Human object at ...>
assert isinstance(p1, Human) == True
assert isinstance(p2, Human) == False

# 補充說明
# type() 方法給3個參數等同於建立名為第一個參數的 class
# type('Human', (), dict(a=1, b=2)) 等同
# class Human:
#   a = 1
#   b = 2
# 
# 但我們可以看到 assert isinstance(p2, Human) == False 
# 也就是實際上 p2 不是 Human 的物件

assert isinstance(human_obj, Human) == True
assert isinstance(human_obj, object) == True
assert isinstance(human_obj, type) == False

# 因此，上面的程式表示 Human class 和 Python 中的所有其他 class 都是 class type 的 object。這種 type 是一個 class，不同於回傳 object type 的 type function。從中建立所有 class 的 type class 在 Python 中稱為 Metaclass。讓我們進一步了解 Metaclass。




# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
# ☆☆☆       Python 中的 Metaclass       ☆☆☆
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆


# Metaclass 是一個 class，這個 class 初始化後可以得到其他 class，或者說 Metaclass 是所有 class 的 class。
# 這從 assert isinstance(Human, type) == True 可以確認

# 在之前，我們檢查了變數 a 和 b 分別是 class int 和 float 的 object。由於 int 和 float 是 class，因此它們應該具有建立它們的 class 或 Metaclass。

type(int)       # < class 'type'>
type(float)     # < class 'type'>
type(object)    # < class 'type'> 甚至 object class 的 type 也是 type
type(type)      # < class 'type'> 甚至 type class 的 type 也是 type

# 因此，type class 是 int 和 float class 的 Metaclass。type class 甚至是 object class 的 Metaclass，而我們知道 object class 是 Python 中所有 class 的 base class。由於 type 本身是一個 class，那麼 type class 的 Metaclass 是什麼? 答案是，type class 的 Metaclass 是自己 type(如上所示)

# Metaclass 在我們將在本文後面介紹的 object 建立過程中起著至關重要的作用。



# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
# ☆☆☆       到目前為止，我們已經涵蓋的兩個重要概念如下：       ☆☆☆
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆

# 1. Python 中的所有 class 都是 type class 的 object，這個 type class 稱為 Metaclass。
# 2. 預設 Python 中的每個 class 都繼承自 object base class。





# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
# ☆☆☆       Python 中的 object 初始化過程       ☆☆☆
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆


# 在對 Python 的 Metaclass 和 object 有了基本的了解之後，我們現在來了解一下 Python 中 object  的建立和初始化的過程。考慮 Human class，定義如下：

class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
print(Human.__new__)
# <built-in method __new__ of type object at 0x00007FFA8D99B780>

human_obj = Human("Leo", "Cheng")

assert isinstance(human_obj, Human) == True
assert isinstance(human_obj, object) == True
# 因為 Human 也繼承自 object，所以 isinstance(human_obj, object) 為 True


# 根據 Human class 的定義，我們不從 __init__ 方法回傳任何東西；
# 那這樣呼叫 Human class 是怎麼回傳 human_obj?
# 我們知道 __init__ 方法是用來初始化 object 的，但是 __init__ 方法是怎麼得到 self 的呢?
# 在本節中，我們將詳細討論這些問題中的每一個並回答它們。

# 在 Python 中建立 object 是一個兩步過程。第一步，Python 建立 object ，第二步，初始化 object 。大多數時候，我們只對第二步感興趣(即初始化步驟)。Python 在第一步(即建立  object )中使用 __new__ 方法，在第二步(即初始化)中使用 __init__ 方法。

# 如果 class 沒有定義這些 method，則它們是從 object base class 繼承來的。由於 Human class 沒有定義 __new__ 方法，所以在 object 建立的過程中，會呼叫繼承自 object class 的 __new__ 方法，而初始化時會呼叫 Human class 的 __init__。接下來，我們將詳細介紹這些 method 中的每一種。




# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
# ☆☆☆      __new__()方法      ☆☆☆
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆


# __new__ 方法是建立 object 過程的第一步。它是 object class 的靜態 method，接受 cls (或稱 class reference) 作為第一個參數。其餘參數(Leo 和 Cheng)在呼叫 class - Human("Leo", "Cheng") 時傳遞。__new__ 方法建立一個 cls type 的 instance(它藉由呼叫 super class，即 object class 的 __new__ 方法，使用語法 super().__new__(cls)，來為 object 配置記憶體)。接著它回傳 cls type 的實例(instance)。

# 通常 __new__ 方法不進行任何初始化，因為這是 __init__ 方法的工作。但是，當我們覆寫 __new__ 方法 時，我們也可以使用它來初始化 object 或在回傳之前根據需要修改它。

# __new__ 方法的 signature

# cls - 為必要參數，__new__ 方法回傳的 object 為 type cls
#
# @staticmethod 
# def __new__(cls[,...]):
#    pass

# 我們可以藉由覆寫 __new__ 方法來修改 object 建立的過程如下

class Human:
    
    def __new__(cls, first_name=None):
    # 建立的 object 的 type 為 cls
    # 我們必須呼叫 object class 的 __new__ 方法來配置記憶體
        obj = super().__new__(cls) # 等同 object.__new__(cls)

        # 修改建立的 object 
        if first_name:
            obj.name = first_name
        else:
            obj.name = "Victor"

        print(type(obj)) # <__main__.Human object at 0x103665668>
        
        return obj # 回傳 object    

# 建立 object 
# object class 的 __init__ 方法會呼叫，因為 Human 沒有定義 __init__
vic = Human()

print(vic.name) # Victor

Sonia = Human("Sonia")
print(Sonia.name) # Sonia


# 在上面的例子中，我們覆寫了 object class 的 __new__ 方法。它接受第一個參數作為 cls - 對 Human class 的 class reference。

# __new__ 方法是 Python 中的一個特例。雖然它是 object class 的靜態 method，但在覆寫它時，我們不必用 @staticmethod 裝飾器裝飾它。

# 在 Human class 的 __new__ 方法中，我們首先使用 super().__new__(cls) 呼叫 object class 的 __new__。object class 的 __new__ 方法建立並回傳 cls class 的實例(instance)。

#我們必須在覆寫的 __new__ 方法中呼叫 object class 的 __new__ 方法來建立 object 並為 object 配置記憶體。

# Human class 的 __new__ 方法修改 object class 的 __new__ 方法回傳的 obj 並為其增加一個 name 屬性。因此，使用 Human class 建立的所有 object 都將具有 name 屬性。我們修改了 Human class 的 object 建立過程。

# 讓我們考慮另一個例子。在此例子中，我們正在建立一個名為 Animal 的新 class 並覆寫 __new__ 方法。這裡當我們從 Animal 類別的 __new__ 方法呼叫 object class 的 __new__ 方法時，我們不是將 Animal 的 class reference 作為參數傳遞給 object class 的 __new__ 方法，而是傳遞 Human 的 class reference。因此，從 object class 的 __new__ 方法回傳的 object 將是 Human type 而不是 Animal type。結果，呼叫 Animal class (即 Animal())回傳的 object 將是 Human type。

class Animal:
    def __new__(cls):    
        obj = super().__new__(Human) # 等同 object.__new__(Human)

        print(f"Type of obj: {type(obj)}") # Type of obj: < class '__main__.Human'>

        return obj

cat = Animal()
# Type of obj: < class '__main__.Human'>
type(cat)  # Output: < class '__main__.Human'>



# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
# ☆☆☆     __init__()方法      ☆☆☆
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆

# __init__ 方法是 Python 中 object 建立過程的第二步。它將第一個參數作為從 __new__ 方法回傳的 object 或 instance。其餘參數是呼叫 class (Human("Leo", "Cheng")) 時傳遞的參數。這些參數用於初始化 object 。__init__ 方法不得回傳任何內容。如果我們嘗試使用 __init__ 方法回傳任何內容，它將會引發 exception，如下所示：

try:

    class Human:
        def __init__(self, first_name):
            self.first_name = first_name
            return self

    human_obj = Human('Leo')
    # Output: TypeError: __init__() should return None, not 'Human'
except:
    pass


class Human:
    def __new__(cls, *args, **kwargs):
    
        print("Inside new method ")
        print(f"args arguments {args}")
        print(f"kwargs arguments {kwargs}")
    
        human_obj = super(Human, cls).__new__(cls)

        print(f"human_obj instance - {human_obj}")
        return human_obj
  
    def __init__(self, first_name, last_name):
        print("Inside __init__ method ")
        # self = human_obj 由 __new__ 方法回傳

        self.first_name = first_name
        self.last_name = last_name

        print(f"human_obj instance inside __init__ {self}: {self.first_name}, {self.last_name}")

human_obj = Human("Leo", "Cheng")

# 在上面的程式中，我們覆寫了 object class 的 __new__ 和 __init__ 方法。__new__ 方法建立 Human class type 的 object (human_obj) 並回傳它。一旦 __new__ 方法完成，Python 就會呼叫 __init__ 方法，並將 human_obj 這個 object 作為第一個參數。__init__ 方法初始化 human_obj，first_name 為 Leo，last_name 為 Cheng。由於 object 建立(object creation)是第一步，初始化(initialization)是第二步，所以 __new__ 方法總是在 __init__ 方法之前被呼叫

# __init__ 和 __new__ 方法在 Python 中都被稱為 magic method。magic method 的名稱以 __(雙下劃線或“dunder”)開頭和結尾。magic method 由 Python 隱含地呼叫；我們不必明確地呼叫它們。例如，__new__ 和 __init__ method 都被 Python 隱含地呼叫。讓我們再介紹一個 magic method，__call__。

# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
# ☆☆☆     __call__()方法      ☆☆☆
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆

# __call__ 方法是 Python 中的一個 magic method，用於使 object 變得 callable。callable object 是可以呼叫的 object 。例如，函數(function)是callable object，因為它們可以使用圓括號呼叫。

# 考慮以下範例：

def print_function():
  print("I am a callable object")

print_function() # function 為 callable

a = 10

try:
    a()  # Output: TypeError: 'int' object is not callable
except:
    pass

#    
# callable()
# 

# callable() 函數用於確定 object 是否可呼叫。callable() 函數將 object reference 作為參數，如果 object  看起來是callable，則回傳 True，如果 object 不可呼叫，則回傳 False。
# 如果可呼叫函數回傳 True，則該 object 可能不可呼叫(?)；但是，如果它回傳 False，則該 object 肯定不可呼叫。(這點很怪)

assert callable(print_function) == True   
assert callable(a) == False               
assert callable(Human)  == True           

# 如上所示，Python 中的 class 是 callable，而且它們應該是！你不這麼認為嗎? 當我們呼叫該 class 時，它回傳該 class 的 instance。讓我們看看從該 class 建立的 object 是否可呼叫。

human_obj = Human("Leo", "Cheng")
assert callable(human_obj) == False

# 我們可以看到 human_obj 不是 callable

# 為了使 Python 中的任何 object 都可呼叫，Python 提供了 __call__ 方法， object 的 class 需實做該方法。例如要使 human_obj object 可呼叫，Human class 必須實做 __call__ 方法。一旦 Human class 實現了 __call__ 方法，就可以像函數一樣呼叫 Human class 的所有 object (使用圓括號)。

class Human:
    def __init__(self, first_name, last_name):
        print("I am inside __init__ method ")
        self.first_name = first_name
        self.last_name = last_name

    def __call__(cls):
        print("I am inside __call__ method ")

human_obj = Human("Leo", "Cheng")
human_obj()
human_obj.__call__()
assert callable(human_obj) == True

# 上面的程式顯示，在 Human class 上實做了__call__ 方法後，human_obj 就變成了一個可呼叫 object。我們可以使用()呼叫 human_obj(即 human_obj())。當我們使用 human_obj() 時，Python 在背後呼叫 Human class 的 __call__ 方法。因此，我們也可以直接呼叫 human_obj 上的 __call__ method (​​即 human_obj.__call__())，而不是將 human_obj 呼叫為 human_obj()。human_obj() 和 human_obj.__call__() 是相同。

# 對於所有 callable 物件，它們的 class 必須實做 __call__ 方法。

# 我們知道函數是一個可呼叫物件，所以 function class 必須實做 __call__ 方法。讓我們在前面定義的 print_function 上呼叫 __call__ 方法。

print_function.__call__()  
# Output: I am a callable object

# In Python, class is also a callable object; therefore, it is a class 's class (Metaclass ) (i.e., the type class must have a call method defined on it). Hence, when we call Human(), in the background, Python calls the call method of the type class .

# 在 Python 中，class 也是一個可呼叫物件；因此，它是一個 class 的 class (Metaclass)(也就是說，type class 必須定義一個 __call__ 方法 )。因此，當我們呼叫 Human() 時，Python 會在背後呼叫 type class 的 __call__ method。

# 粗略地說，type class 上的 __call__ 方法如下所示。這僅用於解釋目的；我們將在後面介紹 __call__ 方法的實際定義。
'''
class type:
    def __call__():
        # Called when class is called i.e. Human()
        print("type's call method ")
'''
# 了解了 __call__ 方法以及呼叫 class 時如何呼叫 type class 的 __call__ 方法之後，讓我們找出以下有關物件 初始化過程的問題的答案：

''' 2023-0

#
# 問題 : 誰呼叫了 __new__ 和 __init__ 方法 ?
# 問題 : 誰將 self 物件傳遞給 __init__ 方法 ?
#

# 由於__init__ 方法是在__new__ 方法之後呼叫的，而__init__ 方法沒有回傳任何東西，呼叫 class 時是如何回傳物件的(即呼叫 Human class 如何回傳 human_obj 物件)?
# 考慮一個在 Python 中 instance 化 object 的示例。

class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

human_obj = Human("Leo", "Cheng")

# 我們知道，當我們呼叫 class (即 Human("Leo", "Cheng"))時，會呼叫 type class 的 __call__ 方法。但是，type class 的 __call__ 方法的定義是什麼?當我們談論 CPython 時，type class 的 __call__ 方法定義是用 C 語言定義的。如果我們把它轉換成 Python 並簡化它，它看起來有點像這樣：

# type 的 __call__ 方法，當我們呼叫 Human() 時會呼叫
def __call__(cls, *args, **kwargs):
  # cls = Human class 
  # args = ["Leo", "Cheng"]
  # 呼叫 Human class 的 __new__ 方法，但因為 Human 沒有定義 __new__ 方法
  # 所以會改呼叫 object class 的 __new__ 方法
  human_obj = cls.__new__(*args, **kwargs)

  # 在 __new__ 方法回傳物件後，__init__ 方法只有在以下情況會被呼叫
  # 1. human_obj 非 None
  # 2. human_obj 是 Human class 的實例(instance)
  # 3. Human class 有定義 __init__ 方法
  if human_obj is not None and isinstance(human_obj, cls) and hasattr(human_obj, '__init__'):
    # 當 human_obj 呼叫 __init__ 時，__init__ 方法中 self 就是 human_obj 
    human_obj.init(*args, **kwargs)

  return human_obj

# 讓我們理解上面的程式；當我們在背後執行 Human("Leo", "Cheng") 時，Python 將呼叫 type class 的 __call__ 方法，該方法的定義類似於上面的程式片段。如上所示，type class 的 __call__ 方法接受 Human class 作為第一個參數(cls 是 Human class)，其餘參數在呼叫 Human class 時傳遞。type class 的 __call__ 方法將首先呼叫定義在 Human class 上的 __new__ 方法，如果有的話；否則，呼叫 Human class 的父類別的 __new__ 方法(​​即 object class 的 __new__ 方法)。__new__ 方法將回傳 human_obj。現在，type class 的 __call__ 方法將以 human_obj 作為第一個參數呼叫定義在 Human class 上的 __init__ method。__init__ 將使用傳遞的參數初始化 human_obj，最後，__call__ 方法將回傳 human_obj。

#
# Python中的 object 建立 instance過程
#

# 因此，在 Python 中建立和初始化物件時遵循以下步驟：

# 呼叫 Human() 時，在背後會呼叫 type class 的 __call__ 方法(​​即 type.__call__(Human, "Leo", "Cheng"))。type.__call__ 將首先呼叫定義在 Human class 上的 __new__ 方法。如果 Human class 上沒有定義 __new__ 方法，就會呼叫 object class 的 __new__ 方法。__new__ 方法將回傳 Human type 的物件 human_obj。

# 現在，type.__call__ 將以 human_obj 作為第一個參數呼叫定義在 Human class 上的 __init__ 方法。這個 human_obj 將是 __init__ 方法 中的 self。
# __init__ 方法將 human_obj 初始化為 first_name 作為 Leo，last_name 作為 Cheng。__init__ 方法不會回傳任何東西。
# 最後，type.__call__ 將回傳 human_obj 。
# 根據 type.__call__ 的定義，每當我們建立一個新物件時，總會呼叫 __new__ 方法，但呼叫 __init__ 方法 取決於 __new__ 方法的輸出。只有當 __new__ 方法回傳一個 Human class 或 Human class 的子 class type 的物件時，才會呼叫 __init__ 方法。

#
# 讓我們了解一些案例。
#

# Case 1：如果 __new__ 方法回傳的物件是 Human type (即 __init__ 方法的 class )，則將呼叫 __init__ 方法。

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
        print(f"Ended: __init__ method of Human class ")

human_obj = Human("Leo", "Cheng")

# Creating the object with cls: < class '__main__.Human'> and args: ('Leo', 'Cheng')
# Object created with obj: <__main__.Human object at 0x102f6a4e0> and type: < class '__main__.Human'>
# Started: __init__ method of Human class with self: <__main__.Human object at 0x102f6a400>
# Ended: __init__ method of Human class with self: <__main__.Human object at 0x102f6a400>

# Case 2: 如果 __new__ 沒有回傳，那麼 __init__ 不會呼叫

class Human:
    def __new__(cls, *args, **kwargs):
        print(f"Creating the object with cls: {cls} and args: {args}")
        obj = super().__new__(cls)
        print(f"Object created with obj: {obj} and type: {type(obj)}")
        print("Not returning object from __new__ method , hence __init__ method will not be called")

    def __init__(self, first_name, last_name):
        print(f"Started: __init__ method of Human class with self: {self}")
        self.first_name = first_name
        self.last_name = last_name
        print(f"Ended: __init__ method of Human class ")

human_obj = Human("Leo", "Cheng")

# Creating the object with cls: < class '__main__.Human'> and args: ('Leo', 'Cheng')
# Object created with obj: <__main__.Human object at 0x102f6a5c0> and type: < class '__main__.Human'>
# Not returning object from __new__ method , hence __init__ method will not be called

# 上述程式碼中，Human class 的 __new__ 方法被呼叫。因此，會建立 type Human 的 obj (也就是替 obj 配置記憶體)。 然而，因為 __new__ 方法沒有回傳 human_obj，因此不會呼叫 __init__ 方法。同時，human_obj 也不會有建立的 obj 的 reference，因為 __new__ 方法沒有回傳。

print(human_obj) # Output: None

# Case 3: __new__ 回傳 integer 物件

class Human:
    def __new__(cls, *args, **kwargs):
        print(f"Creating the object with cls: {cls} and args: {args}")
        obj = super().__new__(cls)
        print(f"Object created with obj: {obj} and type: {type(obj)}")
        print("Not returning object from __new__ method , hence __init__ method will not be called")
        return 10

    def __init__(self, first_name, last_name):
        print(f"Started: __init__ method of Human class with self: {self}")
        self.first_name = first_name
        self.last_name = last_name
        print(f"Ended: __init__ method of Human class ")

human_obj = Human("Leo", "Cheng")

# 上述程式碼中，Human class 的 __new__ 方法被呼叫。因此，會建立 type Human 的 obj (也就是替 obj 配置記憶體)。 然而，因為 __new__ 方法沒有回傳 human_obj 反而回傳 integer 10，因此不會呼叫 __init__ 方法。同時，human_obj 也不會有'建立的物件' 的 reference，而是參照到 integer 10。

print(human_obj)
# Output: 10

# 在 __new__ 方法沒有回傳 class 的 instance 的情況下，如果我們要初始化物件，我們需要在 __new__ 方法中明確呼叫 __init__ 方法，如下

class Human:
    def __new__(cls, *args, **kwargs):
        print(f"Creating the object with cls: {cls} and args: {args}")
        obj = super().__new__(cls)
        print(f"Object created with obj: {obj} and type: {type(obj)}")
        print("Not returning object from __new__ method , hence __init__ method will not be called")
        obj.__init__(*args, **kwargs)
        return 10

    def __init__(self, first_name, last_name):
        print(f"Started: __init__ method of Human class with self: {self}")
        self.first_name = first_name
        self.last_name = last_name
        print(f"Ended: __init__ method of Human class ")

human_obj = Human("Leo", "Cheng")

# Creating the object with cls: < class '__main__.Human'> and args: ('Leo', 'Cheng')
# Object created with obj: <__main__.Human object at 0x102f6a860> and type: < class '__main__.Human'>
# Not returning object from __new__ method , hence __init__ method will not be called
# Started: __init__ method of Human class with self: <__main__.Human object at 0x102f6a860>
# Ended: __init__ method of Human class 

# 上述 case 中，__new__ 方法回傳的是 integer 物件，因此 human_obj 的值為 10

print(human_obj)
# Output: 10
#'''
