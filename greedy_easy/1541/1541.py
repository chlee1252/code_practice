equation = input()

numbers = []
operation = []

number = ""
for eq in equation:
    if eq not in "+-":
        number += eq
    else:
        numbers.append(int(number))
        operation.append(eq)
        number = ""
if number != "":
    numbers.append(int(number))

idx = None
for i, v in enumerate(operation):
    if v == '-':
        idx = i
        break

if idx == None:
    print(sum(numbers))
    exit() 
big_nubmer = 0
for i in numbers[idx+1:]:
    big_nubmer += i

print(sum(numbers[:idx+1]) - big_nubmer)