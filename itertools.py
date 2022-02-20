# itertools : product, permutations, combinations, accumulate, groupby, and infinite iterators

# from itertools import product

# a = [1,2]
# b = [3]

# prod = product(a,b) # This willfive the cartesian product of a and b
# print(prod)
# print(type(prod))
# print(list(prod))


# prod = product(a,b, repeat=2) # We can also define a number of repetition
# print(list(prod))

######################################################################
from itertools import permutations

a = [1,2,3]

perm  = permutations(a)
print(list(perm))

perm  = permutations(a, 2) # for shorter length permutation
print(list(perm))