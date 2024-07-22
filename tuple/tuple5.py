

list_data = [(1,2,3,4),("hi", "hello", "byee"),(34, "anime")]

k = 3

output_list = []
for i in list_data:
    if len(i) != k:
        output_list.append(i)
        


print(output_list)