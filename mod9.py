class Coordinate:
    def __set_name__(self, owner, name):
        print('__set_name__', name)
        self._name = name

    def __get__(self, instance, owner):
        print('__get__')
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        print('__set__')
        try:
            instance.__dict__[self._name] = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError(f'"{self._name}" must be a number') from None

class Point:
    x = Coordinate()
    y = Coordinate()

    def __init__(self, x, y):
    
        # print(type(self.x))
        # print(type(self.y))
        Point.x = x
        Point.y = y
        
    # print(type(Point.x))
    # print(type(Point.y))

print(dir(Point.x))    
# p1 = Point(10,20)
# print(p1.x)
