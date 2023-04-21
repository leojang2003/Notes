# 一個簡單的 decorator class

class Wrapper:

    def __init__(self):        
        pass
        
    def __set_name__(self, owner, name):
        self._name = name
        print('Inner owner =', owner, 'name=', name)
        
    def decorate(func):
        
        def inner():
            print('inner started ...')
            func()
            print('inner ended ...')
            
        return inner

class Outer:
    
    # x = Inner(func)
    
    def __init__(self):
        # self._radius = radius
        pass
    
    #@Wrapper.decorate
    def func(self):
        print("i'm home")

    func = Wrapper.decorate(func)        
    
poor = Outer()

print(poor.func())

    
    
