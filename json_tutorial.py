import json

person = {"name": "John", "age": 30, "city": "New York", "titles": ["engineer", "programmer"], "haschildren": False}

personJSON = json.dumps(person)
print(personJSON)

personJSON = json.dumps(person, indent=4, separators=('; ', '= '), sort_keys=True)
print(personJSON)

with open('person.josn', 'w') as file:
    json.dump(person, file, indent=4)