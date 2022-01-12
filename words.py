count = 0
print('count   number')  # 3 spaces
list = [1, 22, 44, 55, 64, 15, 4]
for number in list:
    count = count + 1
    print(f'{count}       {number}') # 7 spaces
# these are more simple to understand:
biggest = max(list)
smaller = min(list)
sum = sum(list)
average = sum/count
print(f'the biggest number of this list is {biggest}')
print(f'the smallest number of this list is {smaller}')
print(f'the sum of this list is {sum}')
print(f'the average of this list is: {int(average)}')