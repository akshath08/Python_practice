
# commom elements in three list using sets 

list1 = ["holo", "divine", 45]

list2 = [35,23,56,"divine",45,"confuse"]

list3 = [45,2, 10]

set1 = set(list1)

set2 = set(list2)

set3 = set(list3)

common_elements = set1.intersection(set2.intersection(set3))

print(common_elements)

elements = set(list1) & set(list2) & set(list3)

print(elements)