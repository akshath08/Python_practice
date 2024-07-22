
# class A():

#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
    
#     def sum(self):
    
#         return self.a + self.b
    
#     def mul(self):

#         return self.a * self.b
    
# class B():

#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def sub(self):
#         return self.a - self.b
    
        
# obj1 = A(3,5)

# print(obj1.sum())

# print(obj1.mul())




# x = 1000
# y = 1000
# #z = 69

# print(x is y)

# print(id(x),id(y))


# def change_str(input_str,old,new):
#     string1= list(input_str)
#     for i in range(len(string1)):
#         if string1[i] == old:
#             string1[i] = new

#     modify = ''.join(string1)
#     return modify

# input_str = input()
# old = "n"
# new = "N"
# modify_str = change_str(input_str,old,new)
# print(modify_str)



# import sys

# print(sys.path)

def factorial(n):

    factorial = 1

    for i in range(1,n+1):
        factorial *= i
    print(factorial)
n = int(input())
factorial(n)
    
    



