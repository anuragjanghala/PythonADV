# Errors and exceptions
# syntax error
# a = 5 print(a)
# print(a))

# exception type error
# a = 5 + '10'

# import error
# import somemodule

# name error
# a = 5
# b = c

# file not found error
# f = open('somefile.txt')


# value error
# a = [1,2,3]
# a.remove(4)
# print(a)


# index error
# a = [1,2,3]
# a[4]


# key error
# my_dict = {'name': 'max'}
# my_dict['age']


# Raising Exception
# x = -5
# if x < 0:
#     raise Exception('x should be positive')


# assertion error
# x = -5
# assert (x>=0), 'x is not positive'


# try except block

try:
    a = 5 / 0
except:
    print('an error happened')
    
try:
    a = 5 / 0
except Exception as e:
    print(e)
    
    
try:
    a = 5 / 0
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up...')