

import os

import re

os.system("ls -l" + ">" + "this.txt")

with open("this.txt","r") as file:
    a = file.readlines()
    #print(a)

# a = str(a)

# print(a)
# print(type(a))

# x = a.split(" ")
# print(x)

output = {}


pattern = "\w+\.\w+"

permission = "\-\w+\-\w+\-\w\-+"

date = "(\w+)\s+(\d+)\s+(\d+:\d+)"

size = "\s+(\d+)\s+(?:Jul|Jun)"




for i in a:

    z = re.findall(pattern,i)
    k = re.findall(date,i)
    p = re.findall(permission,i)

    t = re.findall(size,i)

    # print(t)


    if len(z) > 0:

        b = z[0] 

        output[b] = [p,k,t]


print(output)

