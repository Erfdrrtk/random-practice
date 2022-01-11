largest_so_far = 1
print('before', largest_so_far)
list1 = [1, 22, 333, 45, 5, 6]
for number in list1:
    if number > largest_so_far:
        largest_so_far = number
    print(largest_so_far, number)
print('after', largest_so_far)



