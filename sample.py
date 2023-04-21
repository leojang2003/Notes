import mod1
import builtins

# import mod2
# from mod3 import Mod3

# print(dir(mod1))

# obj = mod3.Mod3()
# print(dir(obj))



class animal:
	
	def __init__(self, legs):
		self.legs = legs
		self.num_hands = 4 - legs
		pass
	
	def walk(self):
		print(f'walk with {legs}')
		
	def eat(self):
		print(f'animal eating')

dog = animal(2)

print(globals().keys())
		
# del animal

# print(locals().keys())	
		
class human(animal):

	def __init__(self, legs):
		super().__init__(legs)
		pass
	
	def walk(self):
		print(f'walk with {self.legs} legs')
		
	def hands(self):
		print(f'i have {self.num_hands} hands')
		
	def eat(self):
		animal.eat(self)
		super().eat()
		
# del Animal.walk

# dog = Animal(4)
# dog.walk()




# Monica = Human(3)
# print('Lisa', Lisa.gender)
# print('Monica', Monica.gender)
# Lisa.gender = 'female'
# print('Lisa', Lisa.gender)
# Human.gender = 'LGBT'
# print('Monica', Monica.gender)
# print('Lisa', Lisa.gender)









		
		

# print('-------------------------------')
# print('-------------------------------')
# print('-------------------------------')


# class A:
	# var = 100
	# def print_var(self):
		# print(self)
		# print('var =', self.var)
		# varx = 200
		
		# print(type(A.var))
		
		# def inner_print():
			# print(varx)
			# pass
		# inner_print()		
	
# class Wing:
	
	# def __init__(self):
		# pass
	
	# def fly(self):
		# print('fly with wing')
		
# class Engine:

	# def __init__(self):
		# pass
	
	# def start(self):
		# print('engine starts')
		
# class Airplane(Wing, Engine):
	
	# def __init__(self):
		# pass
		
	# def land(self):		
		# Airplane.fly(self)		
		
	# def fly(self):
		# print(super() is Engine)
		# Wing.fly(self)
		# super().fly()
		# Engine.start(self)
		
# a = Airplane()
# Airplane.fly(a)


# print(builtins.sum(range(0,4)))
# print(__builtins__.sum(range(0,7)))

# print('-------------------------------')

# def mean():
	
	# x = [1,2]
	# print(id(x))
	# def _mean():
		
		# print(id(x))
		# x[0] = 3
		
	# _mean()
	# return x
	
# current = mean()
# print(current)

# people = ['John','Tom']

# def change():
	
	# #people[0] = 'Cena'
	# people = ['Lisa']
	
	
# change()
# print(people)



# print(dir())
# print(dir(mod1))



# print(dir())
# ['__annotations__)


# print(dir(mod1))
# ['__builtins__)



# print('__builtins__')
# print(__builtins__)
# print(type(mod1.__builtins__))

# del raise_exception

# raise_exception()

# l = [1, 2, 3, 4, 5]
# dupe_l = l

# dupe_l = dupe_l[:2]

# print(dupe_l) # [1, 2]
# print(l) # [1, 2, 3, 4, 5] 不受影響，因為 dupe_l[:2] 是回傳一個新的 list




# class Wing:
	
	# def __init__(self):
		# pass

	# def fly(self):
		# print('fly')
		
# class Engine:
	
	# def __init__(self):
		# pass

	# def start_engine(self):
		# print('start_engine')
		

# class Airplane(Wing, Engine):
	
	# def __init__(self):
		# pass
		
	# def fly(self):
		
		# super().fly() # 呼叫父類別方法
		# print('metal wing')
		
# airbus = Airplane()
# airbus.start_engine()
# airbus.fly()


# def bool_return():
    # try:        
        # for x in range(10):
            # if x > 8:
                # break;
            # else:
                # print(x)				
    # finally:
        # print('finally')

# def bool_return2():
    
	# for i in

# bool_return2()
# print(x)

# def divide(x, y):
    # try:
        # result = x / y
    # except ZeroDivisionError:
        # print("division by zero!")
    # else:
        # print("result is", result)
    # finally:
        # print("executing finally clause")

#divide(2, 0)


# class SubException(Exception):
		
	# def __init__(self, *args):
		# self.list = [x for x in args]
			
	# # 覆寫 __str__() 方法
	# def __str__(self):		
		# return '***' + repr(self.list) + '***'

# try:
    # raise SubException('spam)
# print(eggs')
# except Exception as inst:
    
    # print(inst)          
	# # SubException 覆寫 __str__() 方法，print() 顯示如下
	# # ***['spam)
# print(eggs']***
	



# import time
# import random
# import math

# class Person:
	
	# def __init__(self, age, name):
		# self.age = age
		# self.name = name
		
# tom = Person(20, 'Tom Hiddleton')
# tom.weapon = 'Axe'

# weapons = ['Shield)
# print(Sword)
# print(Dagger']

# print('weapon {0.age!a}, name {0.name}'.format(tom))
# print('weapon {x[2]}'.format(x=weapons))
# print('<><<<>>>><><><><><><<><>><<><><>')

# x = 'a'
# y = 2

# print('{0:f}'.format(3))
# print('{0:.0%}'.format(0.3))
# print('{0:f}'.format(31415161743243242423432))
# print('{0:e}'.format(3000.))
# print('{0:#e}'.format(3000.))
# print('{0:c}'.format(4))



# print(str('don toretto\n'))
# print(repr('don toretto\n'))

# # print('{0:0>4.10}'.format("3000.14565"))
# # print("'{0:0=4.3f}'".format(3000.14565))

# # print("'{0:0=6.3F}'".format(3000.14565))
# # print("'{0:0=6.3f}'".format(3000.14565))

# # print("'{0:0=10.3F}'".format(3000.14565))
# # print("'{0:0=10.3f}'".format(3000.14565))

# # print("'{0:0=10.3g}'".format(3000.14565))
# # print("'{0:0=10.3G}'".format(3000.14565))

# # #print("'{0:020_.3f}'".format(3000.14565))

# # print("'{0:<20_}'".format(3000000.14151617))
# # print("'{0:0>#20_}'".format(3000000.14151617))
# # print("'{0:0>5_}'".format(3000000))

# # print('===============================')

# # print("'{0:10}'".format('leojang'))
# # print("'{0:*>10.3}'".format('leojang'))

# # print('===============================')

# # print("'{0:8}'".format('leojang'))
# # print("'{0:8s}'".format('leojang'))
# # print("'{0:>8s}'".format('leojang'))
# # print("'{0:*>8.3s}'".format('leojang'))

# # print("'{0:0>5}'".format(3))
# # print("'{0:0>5}'".format(-3))

# ' 2 '

# while x := random.randint(0,1):
	# print(x)
	# time.sleep(5)
	

# x = 20 + (y := (3+4*2)) - 9

# print(x)
# print(y)

# a1 = [1,2,3]
# a2 = [1,2,]

# print(a1 > a2)





# # # s1 = set('abracadabra')
# # # s2 = set('abc')

# # # a = { x for x in s1 if x not in s2 }
# # # print(a)

# # del dict[1,2]

# # print(dict)

# # x = dict(('a',1),('b',2),('c',3))
# # print(x)

# print('-------------------------------')


# dict = {"c":1,"b":2,"a":3}
# print(list(dict))
# print(sorted(list(dict)))

# def gen2():
	
	# i = 1
	
	# while True:
		# yield i*i
		# i += 1
		

# generator = gen2()

# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))


		
# # for num in gen2():
	# # if(num < 2000):
		# # print(num)
	# # else:
		# # break


