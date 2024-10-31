first = int(input('Enter the number: '))
second = int(input('Enter the number: '))
third = int(input('Enter the number: '))
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif first != second and second != third:
    print(0)
