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