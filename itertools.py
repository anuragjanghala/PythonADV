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
# from itertools import permutations

# a = [1,2,3]

# perm  = permutations(a)
# print(list(perm))

# perm  = permutations(a, 2) # for shorter length permutation
# print(list(perm))



######################################################################
# from itertools import combinations, combinations_with_replacement

# a = [1,2,3,4]

# comb  = combinations(a, 2) # length is mandatory
# print(list(comb))

# comb_wr = combinations_with_replacement(a, 2)
# print(list(comb_wr))



######################################################################
# from itertools import accumulate
# import operator

# a = [1,2,3,4]
# acc = accumulate(a) # by default it will sum
# print(a)
# print(list(acc))

# acc = accumulate(a, func=operator.mul) # it will do mul
# print(a)
# print(list(acc))

# a = [1,2,5,3,4]
# acc = accumulate(a, func=max) # will get max
# print(a)
# print(list(acc))

# a = [2,5,3,1,4]
# acc = accumulate(a, func=min) # will get min
# print(a)
# print(list(acc))


######################################################################
from itertools import groupby


def smaller_than_3(x):
    return x < 3 # will return true or false

a = [1,2,3,4]
group_obj = groupby(a, key=smaller_than_3)
print(group_obj)

for key, value in group_obj:
    print(key, list(value))


    

a = [1,2,3,4]
group_obj = groupby(a, key=lambda x: x<3)
print(group_obj)

for key, value in group_obj:
    print(key, list(value))
    


    
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

group_obj = groupby(persons, key= lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))