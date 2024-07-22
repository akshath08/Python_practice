
# program for adding a tuple to list and vice versa

list1 = ["hi", "hello", 37, 45.8]

tuple1 = ("now", "then", 90, True)

# adding tuple to list

list1.extend(tuple1)

print(list1)

# adding list to tuple

x = list(tuple1)

x.append(list1)

tuple1 = tuple(x)

print(tuple1)


