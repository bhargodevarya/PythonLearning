class Person:

    this_is_a_static_variable = "static variable"

    #constructor
    #self is "this" and should be the first param
    def __init__(self, name):
        self.name = name

    #Instance method which must accept self as the first param    
    def show_name(self):
        print('This name is {0}'.format(self.name))

    def greet_with(self, greeting):
        print("{0} {1}".format(greeting, self.name))

#no new keyword for instance creation
person = Person("Amar")
person.show_name()
person.greet_with("Namaste")