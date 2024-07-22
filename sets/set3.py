
# min and max in a set

numbers = {1,2,3,4,5,6,99,88,25,45}

#print(min(numbers))
#print(max(numbers))
numbers = list(numbers)

minimum = maximum = numbers[0]

for i in numbers[1:]:
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i
print("The maximum is ", maximum)
print("The minimum is ", minimum)