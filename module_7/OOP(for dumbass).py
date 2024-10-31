# a = 5
# b = 17.8
# c = 'cat'
# d = [1, 2, 3]
#
# print(isinstance(d, str))

class Person:
    age = 16
    name = 'Max'

# print(getattr(Person, 'x', 'Impossible'))
# setattr(Person, 'k', 'Lisa')
# delattr(Person, 'age')


print(Person.__dict__)
