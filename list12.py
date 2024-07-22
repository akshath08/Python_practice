
list1 = [1,2,3,4,5,5,7,3]

list2 = []

for i in list1:
   if list1.count(i) > 1:
        
       list2.append(i)
        
print(list2)

# import re

# str = "Im gonna be the king of pirates"

# x = re.match("\D", str)

# print(x)
