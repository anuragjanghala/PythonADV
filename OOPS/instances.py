from item import Item
# from phone import Phone

# Item.instantiate_from_csv()
# print(Item.all)


# but if want to make read only attributes we need use encapsulation

# item1 = Item("myitem", 750)

# print(item1.name)

# setting an attribute
# item1.name = "otheritem"    
# this will only work if we use getters and setters with decorators
# if we dont put setters it will stay read-only

# getting an attribute
# print(item1.name)



# item1._name = "otheritem" # this will work

# print(item1.name)

# print(item1.__name)
# we will make read only attributes in Item class

# print(item1.read_only_name)

# item1.read_only_name = "BBB"  # Error : AttributeError: can't set attribute



###########################################################
# Encapsulation

# item1 = Item("myitem", 750)

# # item1.price = 900

# item1.apply_increment(0.2)

# item1.apply_discount

# print(item1.price)



############################################################
# Abstraction : that shows only necessary attributes hiding unnecessary informations
# hiding unnecessary details from user

# item1 = Item('myitem', 750, 6)

# item1.send_email()

# item1.conenct()  # this will show error as it was hidden cant be accessed by instance.




############################################################
# Inheritance : is a mechanism that allows us to re-use code across classes

# from phone import Phone

# item1 = Phone("AjPhone", 1000, 3)

# item1.apply_increment(0.2)

# print(item1.price) # even this works showing inheritance works

# item1.send_email() # shows no error as it was inherit from parent class Item



#############################################################
# Polymorphism : use of single type entity to represent different types in different scenarios.
# many forms

# name = "jim" # str
# print(len(name)) # 3

# some_list = ['some','name'] # list
# print(len(some_list)) # 2
# # that's polymorphism in action, a single function does know
# # how to handle different kinds of objects as expected!

from keyboard import Keyboard

item1 = Keyboard("jsckeyboard", 1000, 3)

item1.apply_discount()

print(item1.price) # this will works and shows polymorphism
# we can control this discount by providing new pay_rate to class of keyboard show how much we can control