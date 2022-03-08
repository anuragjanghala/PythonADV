
# this type of copy doesn't work with mutable objects
org = [0, 1, 2, 3, 4]
cy = org
cy[0] = -10
print(cy)
print(org)


# shallow copy: one level deep, only references of nested child objects
# deep copy: full independent copy

import copy

org = [0, 1, 2, 3, 4]
cy = copy.copy(org)
cy[0] = -10
print(cy)
print(org)

# for list
cy = list(org)
print(cy)
print(org)
cy = org[:]
print(cy)
print(org)
cy = org.copy()
print(cy)
print(org)

# shallow copy
org = [[1,2],[2,3]]
cy = copy.copy(org)
cy[0][1] = -10
print(cy)
print(org)

# deep copy
org = [[1,2],[2,3]]
cy = copy.deepcopy(org)
cy[0][1] = -10
print(cy)
print(org)


# for class

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
class Company:
    def __init__(self,boss,employee):
        self.boss = boss
        self.employee = employee

# p1 = Person('aj', 23)
# # p2 = p1
# # p2.age = 28
# # print(p2.age)
# # print(p1.age)

# p2 = copy.copy(p1)
# p2.age = 28
# print(p2.age)
# print(p1.age)

p1 = Person('AJ', 23)
p2 = Person('John', 27)

company = Company(p1, p2)
company_clone = copy.copy(company)

# company_clone.boss.age = 24

print(company_clone.boss.age)
print(company.boss.age) # results same as we did only shallow copy and age is at level 2 for that we need deep copy


company = Company(p1, p2)
company_clone = copy.deepcopy(company)

company_clone.boss.age = 24

print(company_clone.boss.age)
print(company.boss.age) 