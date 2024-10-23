def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    print(operand_1, operand_2, operation)


with open('data.txt', 'r') as file:
    for line in file:
        calc(line)
