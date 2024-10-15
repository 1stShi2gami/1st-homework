from pprint import pprint

name = 'sample2'
file = open(name, 'r') # r- read, w - write, a - append
print(file.tell())
pprint(file.read())
print(file.tell())
file.close()
