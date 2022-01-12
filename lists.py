# lists : ordered, mutable, allows duplicate elements

mylist = ['banana', 'cherry', 'apple']
print(mylist)

mylist2 = list()
print(mylist2)

mylist3 = [5, True, 'apple', 'apple']
print(mylist3)

item = mylist[1]
print(item)

item2 = mylist3[-2]
print(item2)

for i in mylist:
    print(i)
    
if 'banana' in mylist:
    print('Yes')
else:
    print('No')
    
print(len(mylist))

mylist.append('lemon')
print(mylist)

mylist.insert(1, 'blueberry')
print(mylist)

item3 = mylist.pop()
print(item3)
print(mylist)

item4 = mylist.remove('cherry')
print(mylist)

# item5 = mylist.clear() # to clear the whole list

mylist.reverse()
print(mylist)

mylist = [4,3,1,-1,-5,10]
mylist.sort() # this will sort the original list
print(mylist)


mylist = [4,3,1,-1,-5,10]
new_list = sorted(mylist) # this will create new sorted list & original remains same
print(new_list, mylist)


mylist = [0] * 5
print(mylist)

mylist2 = [1,2,3,4,5]
new_list = mylist + mylist2 # concatenation
print(new_list)

# slicing
mylist = [1,2,3,4,5,6,7,8,9,10]
a = mylist[1:5]
print(a)

a = mylist[:5]
print(a)

a = mylist[1:]
print(a)

a = mylist[::-1]
print(a)


list_org = ['banana', 'apple', 'cherry']

list_cpy = list_org

list_cpy.append('lemon')

print(list_cpy)
print(list_org) # here both list changes when we changed copy list due to assignment

list_org = ['banana', 'apple', 'cherry']

list_cpy = list_org.copy()
list_cpy.append('lemon')

print(list_cpy)
print(list_org) # here it doesnt as we used copy function

# 2nd option
list_cpy = list(list_org)

# 3rd Option
list_cpy = list_org[:]


# LIST COMPREHENSION
mylist = [1,2,3,4,5,6]
b = [i*i for i in mylist] 
# syntax [{expression} {for loop {x} in {list}}]

print(mylist)
print(b)



# EVERY PRINTED RESULTS:
# ['banana', 'cherry', 'apple']
# []
# [5, True, 'apple', 'apple']
# cherry
# apple
# banana
# cherry
# apple
# Yes
# 3
# ['banana', 'cherry', 'apple', 'lemon']
# ['banana', 'blueberry', 'cherry', 'apple', 'lemon']
# lemon
# ['banana', 'blueberry', 'cherry', 'apple']
# ['banana', 'blueberry', 'apple']
# ['apple', 'blueberry', 'banana']
# [-5, -1, 1, 3, 4, 10]
# [-5, -1, 1, 3, 4, 10] [4, 3, 1, -1, -5, 10]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
# [2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [2, 3, 4, 5, 6, 7, 8, 9, 10]
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# ['banana', 'apple', 'cherry', 'lemon']
# ['banana', 'apple', 'cherry', 'lemon']
# ['banana', 'apple', 'cherry', 'lemon']
# ['banana', 'apple', 'cherry']
# [1, 2, 3, 4, 5, 6]
# [1, 4, 9, 16, 25, 36]