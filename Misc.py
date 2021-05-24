# *args means var args of java

def func(*args):
    print('as a tuple', args)
    print('not as tuple', *args)

func(1,2,3,4)

# **kwargs means all named params passed to a function
def kwargsFunc(**kwargs):
    print(kwargs.pop('a', 'not_found'))
    print(kwargs)

kwargsFunc(one_param=1)