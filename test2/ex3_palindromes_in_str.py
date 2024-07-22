
# Python3 code to demonstrate working of
# Get all substrings of string
# Using list comprehension + string slicing

# initializing string 
test_str = input("Enter the input string : ")

# printing original string 
# print("The original string is : " + str(test_str))

# Get all substrings of string
# Using list comprehension + string slicing
res = [test_str[i: j+1] for i in range(len(test_str))
		for j in range(i, len(test_str))]
# res = test_str.split()

# printing result 
# print("All substrings of string are : " + str(res))

print("The length of substrings are ", len(res))

len3_list = filter(lambda x: len(x) > 2 , res)

len3_list = list(len3_list)

print("the length of elemnts of size greater than 3 are" , len(len3_list))
# print(list(len3_list))

empty_list = []


# def palindrome():
#     palindromes_list = []
#     for i in len3_list:
#         if len3_list[i] == len3_list[::-1]:
#             palindromes_list.append(i)
#             print(palindromes_list)
#         else:
#             pass
            
# for i in len3_list:

#     var = i[::-1]
#     if i == var:
#         empty_list.append(i)

# print(empty_list)



def palindrome():
    for i in len3_list:
        var = i[::-1]
        if i == var:
            empty_list.append(i)
    print("The possible palindromes in the given input sting is ",empty_list)
    print("the no of possible palindromes are : ",len(empty_list))

    


palindrome()



