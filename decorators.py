# two different decorators: function and class

# decorator takes another function as argument and extends the behaviour of this function without explicitly modifying it

# it allows to add new functionality without changing existing one


import functools


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

# def start_end_decorator(func):
    
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('start')
#         res = func(*args, **kwargs)
#         print('end')
#         return res
#     return wrapper

# def debug_decorator(func):
    
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#     return wrapper

# @debug_decorator
# @start_end_decorator
# def say_hello(name):
#     greeting = f'Hello, {name}'
#     print(greeting)
#     return greeting

# say_hello('Alex')


#################################################################

# Class Decorators : they are typically used when we wanted to maintain and update a state

# when we decorate a function with a class, that function becomes an instance of the class.

# When we decorate a function with a class, the function is automatically passed as the first argument to the init constructor.

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'this is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

# cc = CountCalls(None)
# cc()

# classes that decorate functions can either accept arguments or fall back to a default if no argument is passed. 
# here we didn't use argument while calling decorator

@CountCalls
def say_hello():
    print('hello')
    
say_hello()
say_hello()