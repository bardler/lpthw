#messing with lists and dicts
list1 = ['a', 'b', 'c', 'd', 'e']
dict1 = {'alph1':['a', 'b', 'c', 'd', 'e'], 'entry1': "bogus value"}
dict2 = {'alph2': list1, 'entry2': "bogus value 2"}

print list1
print dict1
print dict2

def func():
    print "this just prints bullshit"
    return "Nice string"

dict3 = {'junk': 'more of it',
         'waste': 'less of it',
         'function': func(),
         'print': (10 * 20 - 44 + 10 * 50)
        }

print dict3