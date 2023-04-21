# 這裡的 user:str.tlte('jane dole')='tbd' 只是為了顯示 user 的欄位為 str
# str.title('jane dole') 就是 'Jane Dole'
# user:str.title('jane dole')='tbd' 等同 user:'Jane Dole'='tbd' 等同 user:str ='tbd'
# user 後面接隨便一個字串，Python 可以有彈性的取得該物件的 type 作為參數的預設型別
def test_func(distance:int, user:str='tbd', *, type='train', **kwargs) -> str:	
	
	result = ''
			
	result = result + ' distance = ' + str(distance)
	result = result + ' user = ' + user
	result = result + ' type = ' + type	
		
	return result

print(test_func.__kwdefaults__) # {'type': 'train'}

print(test_func(15))            #  distance = 15 user = tbd type = train

# 修改 annotation
test_func.__kwdefaults__['type'] = 'airplane'
test_func.__kwdefaults__['count'] = 60

print(test_func.__kwdefaults__) # {'type': 'airplane', 'count': 60}
# 多了一個 count，但沒用到

print(test_func(15))            # distance = 15 user = tbd type = airplane

def test_func(distance:int, user:str, *, type='train', **kwargs) -> str:	
	
	result = ''
			
	result = result + ' distance = ' + str(distance) 
	result = result + ' user = ' + user
	result = result + ' type = ' + type	
		
	return result

print(test_func(distance='wang', user='400'))
