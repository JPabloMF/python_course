# DICTIONARIES __________________________________
dictionary = {'name': 'Pepe', 'age': '25', 'city': 'Madrid'}
dictionaryB = {'name': 'Carlos'}
# Get specific value
print(dictionary['name'])
print(dictionary.get('name'))
# Update dictionary
dictionary.update(dictionaryB)
# Get values
print(dictionary.values())
# Get keys
print(dictionary.keys())
# Loop and get values
for key in dictionary:
    print(dictionary[key])
# Clear dictionary
dictionary.clear()
print(dictionary)
