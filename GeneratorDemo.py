from operator import itemgetter


def domain_generator():
    domains = ['gmail', 'yahoo', 'rediffmail', 'rocketmail']
    for item in domains:
        yield item


email = input('enter an email')

if '@' not in email:
    print('Please enter a valid email, domains are', end=' \n')
    for domains in domain_generator():
        print(domains)

# To generate each value
domain_names = domain_generator()
print(next(domain_names))
print(next(domain_names))
print(next(domain_names))
print(next(domain_names))

#Since there are 4 values and the next has been called 4 times.
#The line below raises an exception
print(next(domain_names))