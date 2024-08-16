first = int
second = int
third = int
number = int(input('Enter the number: '))
if number == first == second and second == third:
    print(3)
elif number == first == second or second == third or first == third:
    print(2)
elif number == first != second and second != third and first != third:
    print(0)
else:
    print('не то число ')