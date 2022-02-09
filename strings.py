# Strings : ordered, immutable, text representation

# from re import M, sub


# my_string = 'Hello World'
# print(my_string)

# my_string = 'I\'m a programmer'
# print(my_string)

# my_string = "I'm a programmer"
# print(my_string)

# my_string = """Hello \
# world"""
# print(my_string)

# my_string = """Hello
# world"""
# print(my_string)

# char = my_string[1]
# print(char)

# # my_string[1] = 'E'  # will show error assignment error
# my_string = 'Hello World'
# substring = my_string[1:5]
# print(substring)


# substring = my_string[::-1]
# print(substring)


# greeting = 'Hello'
# # name = 'Tom'
# # sentence = greeting + " " + name
# # print(sentence)

# for i in greeting:
#     print(i)

# if 'e' in greeting:
#     print('yes')
# else:
#     print('no')
    
# if 'ell' in greeting:
#     print('yes')
# else:
#     print('no')


# my_string = '   Hello World     '
# print(my_string)
# my_string = my_string.strip()
# print(my_string)

# print(my_string.upper())
# print(my_string.lower())
# print(my_string.startswith('World'))
# print(my_string.startswith('Hello'))
# print(my_string.endswith('World'))
# print(my_string.find('o'))  # will return index
# print(my_string.find('lo'))
# print(my_string.count('p'))
# print(my_string.replace('World', 'Universe'))

# from timeit import default_timer as timer

# my_string = 'how are you doing'
# my_list = my_string.split(' ')
# print(my_list)
# new_string = ' '.join(my_list)
# print(new_string)
# new_string = ''.join(my_list)
# print(new_string)

# my_list = ['a'] * 1000000 # bad method instead use join method
# # print(my_list)

# start = timer()
# my_string = ''
# for i in my_list:
#     my_string += i
# stop = timer()
# # print(my_string)
# print(stop-start)

# start = timer()
# my_string = ''.join(my_list)
# stop = timer()
# # print(my_string)
# print(stop-start)



# # %, .format() , f-strings

# var = 'Tom'
# my_string = "the variable is %s" % var
# print(my_string)


# var = 10
# my_string = "the variable is %d" % var
# print(my_string)


# var = 1.34234
# my_string = "the variable is %f" % var
# print(my_string)


# var = 'Tom'
# my_string = "the variable is {}".format(var)
# print(my_string)


# var = 1.342342
# my_string = "the variable is {:.2f}".format(var)
# print(my_string)


# var = 'Tom'
# var2 = 'Jerry'
# my_string = f"the variable is {var*2} and {var2}"
# print(my_string)