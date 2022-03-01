# two different decorators: function and class

# decorator takes another function as argument and extends the behaviour of this function without explicitly modifying it

# it allows to add new functionality without changing existing one

from ast import arg
import functools
import re

# @mydecorator
# def dosomething():
#     pass

# def start_end_decorator(func):
    
    # @functools.wraps(func)
    # def wrapper(*args, **kwargs):
    #     print('start')
    #     res = func(*args, **kwargs)
    #     print('end')
    #     return res
    # return wrapper 

# def print_name():
#     print("alex")
    
# print_name()
    
# print_name = start_end_decorator(print_name)

# print_name()


# @start_end_decorator
# def print_name():
#     print("alex")

# # we dont need this line
# # print_name = start_end_decorator(print_name)    
# print_name()


# @start_end_decorator
# def add5(x):
#     return x + 5

# res = add5(10)
# print(res)


# print(help(add5))
# print(add5.__name__) # python got confused as both identities have same name to fix this we functools


# Decorators with arguments

# def repeat(num_times):
    
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat
                

# @repeat(num_times=5)
# def greet(name):
#     print(f'Hello {name}')
    

# greet("John")

#################################################################
# Nested Decorators

def start_end_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        res = func(*args, **kwargs)
        print('end')
        return res
    return wrapper

def debug_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug_decorator
@start_end_decorator
def say_hello(name):
    greeting = f'Hello, {name}'
    print(greeting)
    return greeting

say_hello('Alex')