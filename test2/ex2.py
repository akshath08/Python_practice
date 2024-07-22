

#import timeit

# print(timeit.timeit(stmt ='["red ", "blue", "green",3 ,6]', number=10000000))


# print(timeit.timeit(stmt ='("red ", "blue", "green",3 ,6)', number=10000000))

# Dictionary with a list as a key - Raises a TypeError
# my_dict = {[1, 2]: "value"}  

# Dictionary with a tuple as a key - Works correctly
# my_dict = {(1, 2): "value"}
# print(my_dict[(1,2)])  # Output: value
# tuple of vowels



vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset(()))



# frozensets are immutable
fSet.add('v')