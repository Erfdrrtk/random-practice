rog = [1, 33, 53, 120 ,50 ,6034]
compare = 0

for number in rog:
    if number > compare:
        compare = number
    print(compare, number)
# once the loop is done, the biggest number will be printed
print(f'the biggest number is {compare}')