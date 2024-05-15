dict={1:'a',2:'b',3:'c',4:'d'}
print(dict[1])
dict1=dict.get(2)
print(dict)
print(dict1)
print(dict.keys())
print(dict.values())
print(dict.items())
# Iteration
for key in dict:
    print(key,dict[key])
# Adding items

dict[5]='d'
print(dict)
print(dict.update({5:'e'}))
print(dict)
# set default values
dict.setdefault(6)
print(dict)

# Remove items
dict.pop(6)
print(dict)
# List Compehensions
sqr = {x: x**2 for x in range(1, 6)}
print(sqr)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

even = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even)
# Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

list_ot = [('a', 1), ('b', 2), ('c', 3)]
dict = {key: value for key, value in list_ot}
print(dict)
# Output: {'a': 1, 'b': 2, 'c': 3}
