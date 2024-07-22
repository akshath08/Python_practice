


# # list1 = [34,22,45,43]

# # empty = []

# # for i in list1:
# #     sum1 = 0

# #     for num in str(i) :
# #        sum1 += int(num)
# #     empty.append(sum1)
# # print(empty)+

# # list1 = [1,2,3,{6,9}]
# # # list2 = "string"
# # list3 = {"hi","hello",3}
# # # set1 = {1,2,4}

# # def combine(*args):
# #     list4 = []

# #     for i in list1:
# #         # print(type(i))
# #         if type(i) == set:
# #             for j in i:
# #                 list4.append(j)
# #         elif type(i) == str or int:

# #             list4.append(i)
            
# #     for item in list3:
# #         # if item not in list4:
# #         list4 = list4 + [item]
    

# #     return list4

# # p = combine(list1,list3)     

# # print(p)



    
  
    



# #     for number in numbers:
# #   digit_sum = 0
# #   for digit in str(number):
# #     digit_sum += int(digit)
   

   
    
  
    



# # print(hi) '''Hello world '''


# # view = memoryview(b"hello world")

# # for i in view:
# #     print(i)


# # k = {[256,90],} 
# # p = [{90,8}]
# # print(k)
# # print(p)


# list1 = [1,2,4,{2,4}]

# # set1 = {1,2,3,[4,5]}

# list2 = [12,56,(2,6,7)]

# set2 = {1,34,8,(3,7,8)}

# tuple1 = (4,67,[2,9,0])

# tuple2 = (45,18,7,{10,76})

# set3 = {(23,45),(56,90),(67,69)}

# print(list1)

# # print(set1)

# print(list2)

# print(set2)

# print(tuple1)

# print(tuple2)

# print(set3)


# num = int(input("Enter the number: "))
# def fabbinocci(n):
#     if n < 2:
#         return n
#     else:
#         return fabbinocci(n-1)+fabbinocci(n-2)
# for i in range(num):

#     print(fabbinocci(i))  

# # Write your code below this line 
# def prime_checker(n):
#   if n <=1:
#     print("not prime")
#   for i in range(2,((n//2)+1)):
#     if( n%i == 0):
#       return "It's a prime number."
#     else:
#       return "It's not a prime number."
      


# # Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input()) # Check this number
# var = prime_checker(n)
# print(var)

def sorteing_list():
    list = [1,5,4,2]
    # list2 =[]
    x = len(list) #4
    for i in range(0,x): # 0 end x x-1 
        print("i value : ",i)
        for j in range(i+1,x):
            print(f"i:{i} and j:{j}")
            print(f"list i:{list[i]} and list j:{list[j]}")
            if(list[i] > list[j]): #1 > 5 

                list[i],list[j] = list[j],list[i]
        
    print(list)

sorteing_list()