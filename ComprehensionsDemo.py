# for i in range(1,11):
#     for j in range(1,11):
#         print(i, i*j)

# Produces a list of tuples
#[(1,1),(1,2),(1,3),....(2,2),(2,4),(2,6)....,]
result = [(outer, outer*mult) for mult in range(1,11) for outer in range(1,11)]
print(result)

# Produces a list of list of tuples
#[[(2,2), (2,4), (2,6)....], [(3,3),(3,6), (3,9)...], .....]
result = [[(outer, outer*mult) for mult in range(1,11)] for outer in range(1,11)]
print(result)

sentence = "This my example for a very long sentence. This is actually not that long"

# Same variable as the one used in comprehension
words = ['These', 'are','my', 'words']

# expression iteration
sentence_upper = [words.upper() for words in sentence.split(' ')]

print(sentence_upper)

# Does not override
print(words)

# Comprehensions with conditions
nums = [1,2,3,4,5]
sum_of_even_numbers = [n*n for n in nums if n % 2 == 0]
print(sum_of_even_numbers)

squares_for_even_not_for_odd = [n*n if n % 2 == 0 else n for n in nums]
print(squares_for_even_not_for_odd)