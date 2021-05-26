# Creating a list
my_list = [1,2,3,4]
my_empty_list = []
my_empty_list_2 = list()
another_lsit = list({2, 3, 4, 'q'})

print(my_empty_list_2)

# Appending to a list
my_empty_list.append('appended')

# Deleting an item from a list
# Deleted the 2nd element
del my_list[1]
# Deleted the value 4
my_list.remove(4)
print(my_list)

# Update a list

# Updates the element at that index
my_list[1] = 24
print(my_list)

# Updates a list by adding one more element at the given index and extending the list
my_list.insert(1, 30)
print(my_list)

# Combine 2 lists into 1
# Modifies the existing list
my_list.extend(another_lsit)
print(my_list)

# Creates a new list
new_list = my_list + another_lsit
print(new_list)

# Slicing a list

# Start from the 0 index and get me elements till 3-1
my_list[0:3]

# Start from the 0 index, till the end, pick every 2nd element
print('This is it', my_list[::2])

print('This is till the last', my_list[0:-1])

# For loop-ing a list
ind = 0
while ind < len(my_list):
    print(f'While loop element {my_list[ind]} is at index {ind}')
    ind += 1

ind = 0
for index in range(len(my_list)):
    print(f'For loop, element {my_list[index]} is at index {index}')

# For loop-ing an enumerate of a list
for value,index in enumerate(my_list):
    print(f'Enumerate iteration {value} is at index {index}')


data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here
for items in data:
    item = items.split('-')
    if 'Flower' in item[1]:
        flowers.append(item[0])
    else:
        shrubs.append(item[0])

print(flowers)
print(shrubs)