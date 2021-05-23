# Creation of dictionaries
my_dict = {
    "name" : "Amar",
    "age" : '30',
    'email': 'myemail@gmail.com',
    34: 'random',
    'weight': 85
}

person = {'name': 'Ajay'}
person_dict = dict(person)
print(person_dict)


# inserting in a dictionary
my_dict['address'] = 'Home'

# Updating a dictionary
my_dict['age'] = 16

# Deleting an element from a dictionary
del my_dict['email']

# Get all keys
for keys in my_dict.keys():
    print(keys)

# Get all values
for values in my_dict.values():
    print('value ' , values)

#print(dict)

print(my_dict.pop('age'))

print('address' in my_dict.keys())

for items in my_dict:
    print('item', items)
