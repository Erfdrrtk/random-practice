range1 = int(input('enter the amount of numbers in the list: '))
list1 = []
count = 0

for number in range(range1):
    enter_number = int(input('enter a number: '))
    list1.append(enter_number)
    count = count + 1
    print(count, enter_number)

print('--- The calculations ---')
biggest = max(list1)
smallest = min(list1)
the_sum = sum(list1)
average = the_sum / count

print(f'the biggest number: {biggest}')
print(f'the smallest number: {smallest}')
print(f'the sum: {the_sum}')
print(f'the average: {int(average)}')
