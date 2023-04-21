# 此篇為 Python’s super() considered super! 的內容

import collections
from pprint import pprint

class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info('Setting %r to %r' % (key, value))
        super().__setitem__(key, value)

pprint(LoggingDict.__mro__)   
# (<class '__main__.LoggingDict'>, <class 'dict'>, <class 'object'>)

class LoggingOD(LoggingDict, collections.OrderedDict):
    pass

pprint(LoggingOD.__mro__)
# (<class '__main__.LoggingOD'>,
 # <class '__main__.LoggingDict'>,
 # <class 'collections.OrderedDict'>,
 # <class 'dict'>,
 # <class 'object'>)
 
 # 在 class 使用 super()時, 我們並不知道被呼叫者(callee)會是誰，因為有可能未來又有新增的 subclass
 # 以這裏的例子就是 LoggingOD 這個後來新增的 subclass，改變了 MRO (?)

pprint('LoggingOD.__bases__')
print(LoggingOD.__bases__)
 
try:
 
    class Shape:
        def __init__(self, shapename, **kwds):
            self.shapename = shapename
            for k,v in kwds.items():
                print(k,v)            
            super().__init__(**kwds)        

    class ColoredShape(Shape):
        def __init__(self, color, **kwds):
            self.color = color
            super().__init__(**kwds)

    cs = ColoredShape(color='blue', shapename='triangle')        
    # 上面這樣 ok，參數必須剛好用完
            
    cs = ColoredShape(color='red', shapename='circle', extra='tbd')
    # 這樣 Shape 呼叫 super().__init__(**kwds) 還有個參數 extra
    # extra tbd
    # TypeError: object.__init__() takes exactly one argument (the instance to initialize)
    
except:
    pass

# 設計 ancestor tree 時，叫彈性的作法是，設計 method 自己取自己需要的變數，如上
# ColoredShape 使用 color，Shape 使用 shapename 
# 最後的 **kwds 就是空的，如果不是空的最後呼叫 object.__init__() 會出錯，因為 object.__init__() 不接受參數

# 以上設計方式可以確保 method 的 caller/callee 的參數 pattern 吻合
# 以下為確保 ancestor tree 都有此 method

# 上面的範例展示了最簡單的情況。我們知道 object 有一個 __init__ 方法，並且 object 始終是 MRO  鏈中的最後一個類別，因此一系列對 super().__init__ 的呼叫都保證最後是呼叫 object.__init__ 結束。換句話說，我們保證 super() 調用的目標存在並且不會因 AttributeError 而失敗。

# 對於 object 沒有我們需要的 method 時（例如 draw() method ）的情況，我們需要編寫一個保證在 object 之前呼叫的 root class。root class 的職責只是消化掉 method call，不再呼叫 super()。

# Root.draw 還可以使用 assertion 進行防禦性編程，以確保它不會遮蔽 chain 中稍後的其他 draw() method。如果子類錯誤地繼承了一個具有 draw() 方法但未從 Root 繼承的 class，則可能會發生這種情況：

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

# 如果子類想要將其他 class 注入到 MRO 中，那些其他 class 也需要從繼承自 Root，這樣調用 draw() 的路徑就無法在沒有被 Root.draw 停止的情況下到達 object。這應該清楚地記錄下來，以便編寫新的協作類的人知道從 Root 繼承。這個限制與 Python 自己要求所有新的異常都必須繼承自 BaseException 類似。

class BrokenShape():
    def __init__(self, broken, **kwds):
        self.broken = broken
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  broken shape :', self.broken)
        super().draw()

class ColoredShape(Shape, BrokenShape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super().draw()
        
pprint(ColoredShape.__mro__)
# (<class '__main__.ColoredShape'>,
 # <class '__main__.Shape'>,
 # <class '__main__.Root'>,
 # <class '__main__.BrokenShape'>,
 # <class 'object'>)

 # 我們建立一個沒有沒有繼承 Root 的 class BrokenShape 
try: 
    cs = ColoredShape(color='blue', shapename='square', broken='true')
    cs.draw()
    # AssertionError
except:
    pass

# 交換順序    
class ColoredShape(BrokenShape, Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super().draw()

pprint(ColoredShape.__mro__)        
cs = ColoredShape(color='blue', shapename='square', broken='true')
cs.draw()
