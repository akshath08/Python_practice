
l1 = ['a', 'b', 'c', 'd', 'e']
l2 = ['d', 'e', 'f', 'g', 'h']

s1 = set(l1)

s2  = set(l2)

missing_from_l2 = s1 - s2

print(missing_from_l2)

additional_from_l2 = s2 - s1

print(additional_from_l2)