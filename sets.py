# Sets : unordered, mutable, no duplicates.

# myset = {1,2,3,1,2}
# print(myset) # it wont allow duplications will show {1,2,3}

# myset = set([1,2,3])
# print(myset)

# myset = set("hello")
# print(myset)

# myset = {} # empty dictionary
# print(type(myset))

# myset = set() # empty set
# print(type(myset))

# myset = set()

# myset.add(1)
# myset.add(2)
# myset.add(3)

# # myset.remove(3)
# # myset.remove(4) # it will raise key error

# # myset.discard(3)
# # myset.discard(4) # it wont show any error

# # print(myset.pop())


# # print(myset)


# for x in myset:
#     print(x)
    
# if 1 in myset:
#     print("yes")


# odds = {1,3,5,7,9}
# evens = {0,2,4,6,8}
# primes = {2,3,5,7}

# u = odds.union(evens)
# print(u)

# i = odds.intersection(evens)
# print(i)

# i = odds.intersection(primes)
# print(i)

# i = evens.intersection(primes)
# print(i)

# setA = {1,2,3,4,5,6,7,8,9}
# setB = {1,2,3,10,11,12}

# these wont modify the original sets
# diff = setA.difference(setB)
# print(diff)

# diff = setB.difference(setA)
# print(diff)

# diff = setA.symmetric_difference(setB)
# print(diff)

# to modify
# setA.update(setB) # will add all those from setB which are not in setA
# print(setA)

# setA.intersection_update(setB) # keeping which are in both sets
# print(setA)

# setA.difference_update(setB)
# print(setA)

# setA.symmetric_difference_update(setB)
# print(setA)


# setA = {1,2,3,4,5,6}
# setB = {1,2,3}
# setC = {7,8}

# print(setA.issubset(setB))
# print(setB.issubset(setA))
# print(setA.issuperset(setB))
# print(setB.issuperset(setA))
# print(setA.isdisjoint(setB))
# print(setA.isdisjoint(setC))

# setA = {1,2,3,4,5,6}

# setB = setA # it will change both if we edit any one
# setB.add(7)
# print(setB)
# print(setA)


# setB = setA.copy() # it will not change both if we edit any one
# setB.add(7)
# print(setB)
# print(setA)


# setB = set(setA) # it will not change both if we edit any one
# setB.add(7)
# print(setB)
# print(setA)

# a = frozenset([1,2,3,4]) # immutable form of set
# print(a)

# a.add(7) # will raise error
# but we can use union, intersection, difference methods