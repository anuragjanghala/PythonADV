import random

a = random.random()
print(a) # random float from range 0 to 1

a = random.uniform(1, 10)
print(a) # float range from 1 to 10

a = random.randint(1, 10)
print(a) # integer range 1 to 10

a = random.randrange(1, 10)
print(a) # from 1 to 10 upper bound not included

a = random.normalvariate(0, 1)
print(a) # it will pick random normal of mean of 0 and standard deviation of 1