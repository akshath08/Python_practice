

# # file handling

# file = open("example1.txt","r")

# #file.write("Hi, Monkey D Luffy")
# content = file.read()

# output = {}

# for e in content:
#     for word in e.split():
#         print(word)

#         if word in output:
#             output[word] += 1
#         else:
#             output[word] = 1
# print(output)

# print(type(output))


# #print(content)

# file.close()


output = {}

with open ("example1.txt","r") as file:
    for line in file:
        for word in line.split():
            if word in output:
                output[word] += 1
            else:
                output[word] = 1
            #print(word)
print(output)