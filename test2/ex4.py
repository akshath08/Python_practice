

# def donuts(n,vat):

#     if n > 10:
#         return f"number of {vat} : Many"
#     else:
#         return f"number of {vat} :{n}"

# vat = input()
# a= donuts(11,vat)
# print(a)


# def both_ends(value):
#     if(len(value) < 2):
#         return ""
#     else:
#         v1 =  value[0:2]
#         v2 =  value[-2:]
    
#     return v1+v2
#         # return f"{vat}"    
    
# value = input()
# print(both_ends(value))


# def fix_start(value):
#     count = "*"
#     list1  = []
#     for i in range(len(value)):
#          if var[0] == var[0:]:
#              var [0] = "*"
#              var[1:].replace("b","*")
#     var = value[1:]
#     varr = var.replace("i","*")
#     return value[0]+varr
    


# value  = input()
# print(fix_start(value))




# def mix_up(a,b):
#     var = a[0:2]
#     var2= b[0:2]
#     var3 =a[2:]
#     var4 = b[2:]
#     return f"{var2+var3} {var+var4} "



# a = input()
# b = input()
# print(mix_up(a,b))

# def test(a,b):
#     if a == b:
#         return "Ok"
#     else:
#         return "False"
    
# print(test(5,4))

# def verbing(s):
#     var = "ing"

#     if len(s) >= 3:
#         s = s+var
#     elif len(s) < 3:
#         s = s
#     if s[-3:] != "ing":
#         s = s
#     else:


#     return s


# print(verbing("hailing"))



# def not_bad(s):
#     a = s.find("bad")


# def strings(a,b):
#     a_middle = len(a)/2
#     b_middle = len(b)/2

#     if len(a) % 2 == 1:
#         a_middle = a_middle+1
#     if len(b) % 2 == 1:
#         b_middle = b_middle+1

#     return a[:int(a_middle)] + b[:int(b_middle)] + a[int(a_middle):] + b[int(b_middle):]
    

# a= input()
# b = input()

# print(strings(a,b))



# def str_count(a):
#     count1 = 0
#     for i in a:
#         if len(i) >= 2:
#             if i[0] == i[-1]:
             
#              count1 = count1 + 1

#     return count1
        
# args = ["aa", "aba","cbc", "ba","a"]

# print(str_count(args))

# def string_sort(a):

#     list1 = []
#     for i in a:
#         if i[0] == "x":
#             list1.append(i)

#     a.sort()
#     a.pop(-1)
#     return list1 + a

    

    




# xyy = ["xyc","abs", "mix", "gf"]

# print(string_sort(xyy))
# def myFunc(e):
#     return e[-1]


# def sorted_tuple(a):

#     for i in a:
#         i = list(i)
        




        


# xyy = [(2,4),(9,7),(1,3)]

# # sorted_tuple(xyy)

# print(sorted(xyy,key=lambda k:k[-1]))






# list1 = [1,2,2,4,5,5,9]

# lis2 = []

# for i in list1: # 1 2

#     if i not in lis2: 

#         lis2.append(i)


# print(lis2)




# def prime_factors(n):
#     factors = []
#     d = 2
#     while n > 1:
#         while n % d == 0:
#             factors.append(d)
#             n //= d
#         d += 1
#         if d * d > n:
#             if n > 1:
#                 factors.append(n)
#             break
#     return factors

# # Example usage
# num = int(input("Enter a number to find its prime factors: "))
# result = prime_factors(num)
# print(f"The prime factors of {num} are: {result}")





#print(list1)


# def even_no(n):
#     list1 = []

#     flag = True
#     while flag:
#         list1.append(int(input()))
#         if len(list1) == n:
#             flag = False

#     x = [i for i in list1 if i % 2 == 0]

#     return x

# n = int(input("Enter the Length"))

# print(even_no(n))


# def tup_sum(tup):
#     sum1 = 0
#     tup = list(tup)
#     for i in tup:
#         sum1 += i
#     return sum1

# tup = (2,4,5,6,789,43,45)
# print(tup_sum(tup))




def set_common(s,s1):
    var1 = list(set1)
    var2  = list(set2)
    var3 = []

    for i in var1:
        for j in var2:
            if i == j:
             var3.append(i)
    

    return set(var3)


set1 = {1,2,3,4,5}
set2 = {2,3,6,7,8}

print(set_common(set1,set2))


def dictname(dict1):

    x = list(dict1.values())
    y = list(dict1.keys())
    u = max(x)
    #y = dict1.keys()
    v = x.index(u)
    z = y[v]
    return z
       

dict1 = {"akshath":24,"hemu":23,"sujith":32}
print(dictname(dict1))


