from item import Item
# from phone import Phone

# Item.instantiate_from_csv()
# print(Item.all)


# but if want to make read only attributes we need use encapsulation

item1 = Item("myitem", 750)

print(item1.name)

# setting an attribute
item1.name = "otheritem"    
# this will only work if we use getters and setters with decorators
# if we dont put setters it will stay read-only

# getting an attribute
print(item1.name)






# item1._name = "otheritem" # this will work

# print(item1.name)

# print(item1.__name)
# we will make read only attributes in Item class

# print(item1.read_only_name)

# item1.read_only_name = "BBB"  # Error : AttributeError: can't set attribute