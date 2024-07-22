
list_tuple_example = [("hi",25,45,"ok"), ("me",10),(11,)]

digits_list =[]

for tuple_item in list_tuple_example:
    for item in tuple_item:
        if str(item).isdigit():
            digits_list.append(item)

print(digits_list)

