# print('hello') # ASCII
# print(ord('h'))
# print(ord('e'))
# print(ord('l'))
# print(ord('l'))
# print(ord('o'))
#
# a = 'hello'
# chars = []
# for i in a:
#     chars.append(ord(i))
# s = ''
# for i in chars:
#     s += chr(i)
# print(s)
# print(chars)
print(hex(ord('h')))
bb = b'\x68'
print(bb.decode())