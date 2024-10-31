my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0
elem = my_list[x]
while elem >= 0 and x < len(my_list):
    elem = my_list[x]
    x += 1
    if elem < 0:
        break
    elif elem == 0:
        continue
    print(elem)