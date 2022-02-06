# tuples : ordered, imutable, allows duplicate elements
# mytuple = ("Max", 28, "Boston")
# print(mytuple)

# mytuple = ("Max")
# print(type(mytuple))

# mytuple = ("max",)
# print(type(mytuple))

# mytuple = tuple(["max", 28, "boston"])
# print(mytuple)

# item = mytuple[0]
# print(item)

# item = mytuple[-1]
# print(item)

# mytuple[0] = "Tim"  # ERROR : object does not support item assignment as tuple is immutable


# for i in mytuple:
#     print(i)
    
# if "boston" in mytuple:
#     print("yes")
# else:
#     print("no")


# my_tuple = ('a','p','q','p','l','e')

# # print(len(my_tuple))
# # print(my_tuple.count('p'))
# # print(my_tuple.index('p'))  # will return first occurance
# # print(my_tuple.index('o')) # will show error

# my_list = list(my_tuple)
# print(my_list)

# my_tuple2 = tuple(my_list)
# print(my_tuple2)


# a = (1,2,3,4,5,6,7,8,9,10)

# b = a[2:5]
# print(b)

# b = a[2:]
# print(b)

# b = a[::-1]
# print(b)

# b = a[::2]
# print(b)

# my_tuple = "Max", 28, "Boston"

# name, age, city = my_tuple # the no. of elements must match both sides
# print(name)
# print(age)
# print(city)

# my_tuple = (0,1,2,3,4)

# i1, *i2, i3 = my_tuple
# print(i1)
# print(i3)
# print(i2)


# import sys
# my_list = [0,1,2,'hello',True]
# my_tuple = (0,1,2,'hello',True)
# print(sys.getsizeof(my_list), "bytes")
# print(sys.getsizeof(my_tuple), "bytes")
# # List is larger than Tuple

# import timeit
# print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
# print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))
# # it takes longer time to create 1,000,000 elements list than tuple
# # so working with tuple is more efficient