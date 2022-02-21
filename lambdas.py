# lambda arguments: expression

# add10 = lambda x: x+10
# print(add10(5)) # 15

# # alternative function for lambda function
# def add10_function(x):
#     return x + 10

# mult = lambda x,y: x * y

# print(mult(2, 7)) # 14



# poinst2D = [(1,2), (15,1), (5,-1), (10,4)]
# poinst2D_sorted = sorted(poinst2D)

# print(poinst2D)
# print(poinst2D_sorted)

# poinst2D = [(1,2), (15,1), (5,-1), (10,4)]
# poinst2D_sorted = sorted(poinst2D, key=lambda x: x[1])

# print(poinst2D)
# print(poinst2D_sorted)

# poinst2D = [(1,2), (15,1), (5,-1), (10,4)]
# poinst2D_sorted = sorted(poinst2D, key=lambda x: x[0]+x[1])

# print(poinst2D)
# print(poinst2D_sorted)


######################################################################

# map(function, sequence)

# a = [1,2,3,4,5]
# b = map(lambda x: x*2, a)
# print(list(b))

# # list comprehension
# c = [x*2 for x in a]
# print(c)


######################################################################

# filter(func, seq) # func must return true or false, and filter function must return all the elements for which func evaluates to true

# a = [1,2,3,4,5,6]

# b = filter(lambda x: x%2 == 0, a)
# print(list(b))

# # with list comprehension
# c = [x for x in a if x%2 == 0]
# print(c)


#######################################################################

# reduce(func, seq) # it repeatedly applies the function on sequence till it gets the single value

from functools import reduce
a = [1,2,3,4]

product_a = reduce(lambda x,y: x*y, a)
print(product_a)