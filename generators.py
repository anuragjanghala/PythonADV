# Generators : functions that return an object (lazy iterator) that can be iterated over

# lazy iterators do not store their contents in memory unlike lists
# they generate item one at a time
# they are used to save up  the memory

# Generating an infinite sequence, will require the use of a generator, since your computer memory is finite

# def mygenerator():
#     yield 1
#     yield 2
#     yield 3

# g = mygenerator()
# print(g)

# for i in g:
#     print(i)
    
# val = next(g)
# print(val)

# val = next(g)
# print(val)

# val = next(g)
# print(val)

# val = next(g) # this will raise stopiterator error if we reach all yield statements
# print(val)

# print(sum(g))
# print(sorted(g))

# def countdown(num):
#     print("starting")
#     while num > 0:
#         yield num
#         num -= 1


# cd = countdown(4)

# value = next(cd)
# print(value)
# value = next(cd)
# print(value)
# value = next(cd)
# print(value)
# value = next(cd)
# print(value)
# value = next(cd)
# print(value)

# import sys

# # without generator it takes memory
# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums

# print(firstn(10))
# print(sum(firstn(10)))


# # with generator
# def firstn_gen(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
        
# for i in firstn_gen(10):
#     print(i)
        
# print(sum(firstn_gen(10)))


# #size comparison
# print(sys.getsizeof(firstn(10)))
# print(sys.getsizeof(firstn_gen(10)))

# print(sys.getsizeof(firstn(1_000_000)))
# print(sys.getsizeof(firstn_gen(1_000_000)))



################################################################

def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 21 34 ....
    a, b = 0, 1
    while a<limit:
        yield a
        a, b = b, a+b
        
fib = fibonacci(34)

for i in fib:
    print(i)