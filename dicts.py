# Dictionary : Key-Value Pair, Unordered, Mutable
# mydict = { "name": "max", "age": 28 , "city": "new york" }
# print(mydict)

# mydict2 = dict(name="mary", age=27, city="boston")
# print(mydict2)

# value = mydict["name"]
# print(value)

# # adding more key-value pair to the dict
# mydict["email"] = "abc@email.com"
# print(mydict)

# # if we assign again on same key it will overwrite the existing value
# mydict["email"] = "123@email.com"
# print(mydict)


# # deleting element from dict
# del mydict["name"]
# print(mydict)

# mydict.pop("age")
# print(mydict)

# mydict.popitem() # will remove last element
# print(mydict)


# if "name" in mydict:
#      print(mydict["name"])

# try:
#     print(mydict["lastname"])
# except:
#     print("Error")

# for key in mydict:
#     print(key)
    
# for key in mydict.keys():
#     print(key)    

# for value in mydict.values():
#     print(value)
    
# for key, value in mydict.items():
#     print(key, value)


# mydict_cpy = mydict # this will create impact on orignal if we change anything in copied dict
# print(mydict_cpy)

# mydict_cpy["email"] = "max@email.com" 
# print(mydict_cpy)
# print(mydict)


# mydict_cpy = mydict.copy()
# mydict_cpy["email"] = "max@email.com" 
# print(mydict_cpy)
# print(mydict)


# mydict_cpy = dict(mydict)
# mydict_cpy["email"] = "max@email.com" 
# print(mydict_cpy)
# print(mydict)


# mydict = { "name": "max", "age": 28 , "city": "new york" }
# mydict_2 = dict(name="mary",age=27,city="boston")

# mydict.update(mydict_2)
# print(mydict)

# mydict = {3: 9, 6: 36, 9: 81}
# print(mydict)

# value = mydict[3]
# print(value)

# mytuple = (8,7)

# mydict[mytuple] = 15
# print(mydict)  # this will work as tuple is immutable so hashble whereas list will throw error
# # list can not be used as key but tuple can
# mydict = {mytuple: 15}

# print(mydict)