import json

person = {"name": "John", "age": 30, "city": "New York", "titles": ["engineer", "programmer"], "haschildren": False}

# personJSON = json.dumps(person)
# print(personJSON)

# personJSON = json.dumps(person, indent=4, separators=('; ', '= '), sort_keys=True)
# print(personJSON)

# with open('person.json', 'w') as file:
#     json.dump(person, file, indent=4)

###################################################################
personJSON = json.dumps(person, indent=4, sort_keys=True)

person = json.loads(personJSON)
print(person)

# from json to python with json file

with open('person.json') as file:
    person = json.load(file)
    print(person)