# row=int(input('enter the number of rows:'))
# space=' '
# star='*'
# i=1
# while i<=row:
#     print(space*(row-i),star*(2*i-1))
#     i=i+1
# tuplw = (1,23,4)
# x = (x for x in tuplw if x > 1)
# print()

# n = "enter the number"

# d = n.split(" ")
# # print(d)
# empty = []

# for i in d:
#     empty.append(i)
#     if i == "the":
#         f = i[::-1]
#         empty.append(f)
#     if "the" in empty:
#         y = empty.index("the")
#         empty.pop(y)
#     g = " ".join(empty)
        
# print(g)


    # print(i)

# print(f)
str1 = "is the ree"
x =str1.split(" ")

print(len(str1))
# c = str(x)
# print(type(c))
# print(c)
# y = c.replace("the","eht")
# c = str(y)
# m = ("".join(x))
substring = "is"
stry = " "
for i in x:
    # print(i)

    if i == substring:
        i = "si"
    stry = stry +" "+i
print(len(stry))

