# Object Identity
# 當 Python 建立物件時，像是 variable，function ... 等，檯面下的 Python interpreter 會建立一個獨特的號碼可以識別該物件，當物件不再被參考時，則物件被移除，identity number 也改由其他物件使用。

    
class Student:
    
    name = '' # 建立在此的是 class member，會在 instance 之間分享
    family = {'parent': ''} # 同上
    gender = ''
       
        
    def __init__(self, name, gender, parent):
        
        if(gender == 'male'):
            self.name = name
            self.family['parent'] = parent     
        
    def change_family(self, newFamily):
        self.family['parent'] = newFamily        

    def change_name(self, newName):
        self.name = newName  
        

Kim = Student('Kim', 'female', 'Kim Sr')
print(Kim.__dict__) # {}

print('id(Kim.name) =', id(Kim.name))
print('id(Student.name) =', id(Student.name))

assert id(Kim.name) == id(Student.name) # 都是 ''

Leo = Student('Leo', 'male', 'Leo Sr')
print(Leo.__dict__) # {'name': 'Leo'}


assert id(Student.name) != id(Leo.name) # 因為 Leo.name 指派新的值了
assert Leo.family == Kim.family == {'parent': 'Leo Sr'}
# 注意這裡 Kim 的 family 也變成 {'parent': 'Leo Sr'}
# 這裡我們看到 self.family 都指向 class member 的 family，所以 Kim 的 family 也變成 Leo Sr

Kim.change_family('Tom')
assert Leo.family == Kim.family == {'parent': 'Tom'}
# 同樣變更 Kim 的 family 也會變更到 Leo 的 family

Student.family['zip'] = '75252'
assert Leo.family == Kim.family == {'parent': 'Tom', 'zip': '75252'}


Student.name = 'Jane Dole'
assert Leo.name == 'Leo'
assert Kim.name == 'Jane Dole'
# 注意變更 Class 的 name 時，因為 Kim 尚未指派 name 所以此時 id(Kim.name) = id(Student.name)
# 所以變更 Student.name 同樣會影響 Kim 的 name，但不影響 Leo 的 name

print(Kim.__dict__) # {}
Kim.change_name('Lisa')
print(Kim.__dict__) # {'name': 'Lisa'}
# 呼叫 change_name 會在 Kim 的 instance dict 建立一個名為 name 的變數
assert Leo.name == 'Leo'
assert Kim.name == 'Lisa'
assert Student.name == 'Jane Dole'

# 重點總結!!!
# 在 Python 中的 dot 語法會自動呼叫 __getattribute__()，此方法會優先尋找物件的 internal dictionary(dict)，
# 再來是物件的 type，以上述的情況而言，如果要尋找 Kim.name，就是先執行 Kim.__dict__['name']，再來才是Kim.__class__.__dict__['name']

print(Kim.__dict__['name'])             # Lisa
print(Kim.__class__.__dict__['name'])   # Jane Dole
