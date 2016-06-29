#Study drills for lesson 38

my_int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_string_list = ['test', 'word', 'balls', 'jump']

print my_int_list
print my_string_list

my_string_list.append('work')
print my_string_list

my_string_list.extend('numbers')
print my_string_list

my_int_list.insert(5, 5.5)
print my_int_list

print my_int_list.pop(5)

print my_string_list.index('b')

print my_string_list.count('e')

my_string_list.sort(cmp)
print my_string_list

my_string_list.sort(None)
print my_string_list

test_list = ['a', 'b', 'c', 'd']
print test_list
test_list.reverse()
print test_list