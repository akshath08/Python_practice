


# def n_even(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 0
#     for i in range(n):
#         if i % 2 == 0:

#             print(i)
#     else:
#         pass


        
# print(n_even(99))


# 0 2 4 6 8


# def n_even(n):
#     for i in range(n):
#         if i % 2 == 0:
#             pass
#     return 


# def count_animals(a,b,c):
#     hen = 2
#     cow = 4
#     pig = 4
#     var = hen * a
#     var1 = cow * b
#     var2 = pig * c

#     return var+var1+var2


# print(count_animals(2,5,6))


def pizzzas(n,p):
    dict1 = {
        "batman":[22,30,11,17,15,52,27,12],
        "spider-man":[5,17,30,33,40,22,26,10,11,45]
    }
    count_bat = 0
    count_spi = 0
    x = dict1["batman"]
    y = dict1["spider-man"]
    for values_x in x:
        #print(values_x)
        if values_x >= p:
            count_bat += 1
            
            # if values_x >= n:
            #     print("batman")

    for values_y in y:
        #print(values_y)
        if values_y >= p:
            count_spi += 1
            # if values_y >= n:
            #     print("spider-man")
    
    if count_bat >= n and count_spi >= n:
        return "spider-man & batman"
    elif values_x >= n:
        return "batman"
    elif values_y >= n:
        return "spider-man"
    else:
        pass    
        
n = int(input("Enter the no of pizza :"))

p = int(input("Enter the price of the pizzas : "))

ans = (pizzzas(n,p))

print(ans)
