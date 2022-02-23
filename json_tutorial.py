# import json

# person = {"name": "John", "age": 30, "city": "New York", "titles": ["engineer", "programmer"], "haschildren": False}

# # personJSON = json.dumps(person)
# # print(personJSON)

# # personJSON = json.dumps(person, indent=4, separators=('; ', '= '), sort_keys=True)
# # print(personJSON)

# # with open('person.json', 'w') as file:
# #     json.dump(person, file, indent=4)

# ###################################################################
# personJSON = json.dumps(person, indent=4, sort_keys=True)

# person = json.loads(personJSON)
# print(person)

# # from json to python with json file

# with open('person.json') as file:
#     person = json.load(file)
#     print(person)


###################################################################
import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)


def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Obejct of the type User is not JSON serializable')


userJSON = json.dumps(user, default=encode_user, indent=4)
print(userJSON)

# second method
from json import JSONEncoder

class UserEncoder(JSONEncoder):
    
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
    

userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

userJSON = UserEncoder().encode(user)
print(userJSON)


# from JSON to python object/dict
    
user = json.loads(userJSON)
print(user)
print(type(user)) # dict
print(user['name'])

# for object
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct
    
user = json.loads(userJSON, object_hook=decode_user)
print(user)
print(type(user))
print(user.name)