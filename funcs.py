"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference?)

"""

    
from numpy import number


def print_name(name): # parameters
    print(name)
    
print_name('AJ') # positional argument
print_name(name='AJ') # keyword argument


def foo(a, b, c, d=4): # with default argument for d
    print(a, b, c)


# def foo(a, b=2, c, d=4): # this will raise error
#     print(a, b, c, d)

# foo(1, b=2, 3) # this will raise error
# foo(1, b=2, a=3) # this will also raise error

# args and kwargs
def foo(a, b, *args, **kwargs):
    print(type(args), type(kwargs))
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs [key])
                     
foo(1, 2, 3, 4, 1, six=6, seven=7)
foo(1, 2, six=6, seven=7)
foo(1, 2, 3, 4, 1)


# after * all must be kwargs
def foo(a, b, *, c, d):
    print(a, b, c, d)
    
foo(1, 2, c=3, d=1)


def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)
    
foo(1, 2, 3, last=100)


#################################################

def foo(a,b,c):
    print(a,b,c)
    
my_list=[0,1,2]
foo(*my_list)

    
my_tuple=(0,1,2)
foo(*my_tuple)


my_dict = {'a': 1,'b': 2,'c': 3}
foo(**my_dict)


###############################################
def foo():
    x = number
    print('number inside function:', x)
    
number = 0
foo()



def foo():
    global number
    x = number
    number = 3
    print('number inside function:', x)

number = 0
foo()
print(number)


#################################################
# parameter passing (call by refernce or call by value)

def foo(a_list):
    a_list.append(4)
    a_list[0] = -100

a_list=[1,2,3]
foo(my_list)
print(my_list) # mutable objects can be modified within a function like list and dict


# here a_list will create a local variable due to that my_list wont change
def foo(a_list):
    a_list = [200, 300, 400]
    a_list.append(4)
    a_list[0] = -100
    
my_list = [1, 2, 3]
foo(my_list)
print(my_list)


# this will create local reference
def foo(a_list):
   a_list = a_list + [200, 300, 400]
my_list = [1, 2, 3]
foo(my_list)
print(my_list)


# this will not create local reference
def foo(a_list):
   a_list += [200, 300, 400]
my_list = [1, 2, 3]
foo(my_list)
print(my_list)