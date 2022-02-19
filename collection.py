# collections: Counter, namedtuple, OrderDict, defaultdict, deque
# from collections import Counter
 
# a = 'aaaaaaabbbbbbbbbcccccccccc'
# my_counter = Counter(a)
# print(my_counter)

# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())

# print(my_counter.most_common(2))
# print(my_counter.most_common(2)[0])
# print(my_counter.most_common(2)[0][0])

# print(my_counter.elements())
# print(list(my_counter.elements()))


####################################################################
# from collections import namedtuple

# Point = namedtuple('Point','x,y')

# pt = Point(1, -4)

# print(pt)
# print(pt.x, pt.y)


#####################################################################
from collections import OrderedDict

ordered_dict = OrderedDict()

ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict)

ordered_dict = {} # nowadays this also remember order

ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict)