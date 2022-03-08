# *

print(5*7) # multiplication

print(2 ** 4) # 2 to the power of 4

############################################
zeros = [1]*10
print(zeros)

zeros = [0,1]*10
print(zeros)

zeros = (0,1)*10
print(zeros)

zeros = "AB" * 10
print(zeros)


#############################################
# * in args and kwargs

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    
    for key in kwargs:
        print(key, kwargs[key])
        
foo(1, 2, 3, 4, 5, six=6, seven=7)


def foo(a, b, *, c): # to enforce only kwargs afterwards
    print(a, b, c)
foo(1, 2, c = 3)


################################################
# argument unpacking
def foo(a, b, c):
    print(a, b, c)

my_list = [0,1,2]
foo(*my_list)

my_tuple = (0,1,2)
foo(*my_tuple)

my_dict = {'a': 1, 'b': 2, 'c': 3} 
foo(**my_dict)


numbers = [1,2,3,4,5,6]

*beginning, last = numbers
print(beginning)
print(last)

# if tuple it will still unpack it with list
numbers = (1,2,3,4,5,6)

*beginning, last = numbers
print(beginning) #list
print(last)

beginning, *middle,secondlast, last = numbers
print(beginning)
print(middle)
print(secondlast)
print(last)


# merging lists and tuples
my_dict = [0,1,2]
my_tuple = (1,2,3)
my_set = {4,5,6}

new_list = [*my_dict,*my_tuple,*my_set]
print(new_list)


# merging two dicts

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
my_dict = {**dict_a, **dict_b}
print(my_dict)

dict_a = {'a': 1, 'b': 2}
dict_b = {'a': 3, 'd': 4}
my_dict = {**dict_a, **dict_b}
print(my_dict)