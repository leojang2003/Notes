import logging

logging.basicConfig(level=logging.INFO)

class LoggedAgeAccess:

    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', 'age', value)
        obj._age = value

class Person:

    age = LoggedAgeAccess()             # Descriptor instance

    def __init__(self, name, age):
        self.name = name                # Regular instance attribute
        self.age = age                  # Calls __set__()

    def birthday(self):
        self.age += 1    
        

mary = Person('Mary M', 30)         # The initial age update is logged

# dave = Person('David D', 40)


# vars(mary)                          # The actual data is in a private attribute
# {'name': 'Mary M', '_age': 30}
# vars(dave)
# {'name': 'David D', '_age': 40}

# mary.age                            # Access the data and log the lookup

# mary.birthday()                     # Updates are logged as well

# dave.name                           # Regular attribute lookup isn't logged

# dave.age                          
