
tuple1 = ("a","b","c")
tuple2 = (1,2,3)

combination = []

for i in tuple1:
    for j in tuple2:
        combination.append((i,j))
print(tuple(combination))
