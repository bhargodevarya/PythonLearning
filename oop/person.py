class Person:

    this_is_a_static_variable = "static variable"

    #constructor
    #self is "this" and should be the first param
    def __init__(self, name):
        self.name = name

    @classmethod
    def class_method(cls, num1, num2):
        person = cls(num1+num2)
        print(f'This is a class method {num1+num2}')
        print(Person.this_is_a_static_variable)

    @staticmethod
    def static_method(num1, num2):
        print('This is the static class')
        print(Person.this_is_a_static_variable)   

    #Instance method which must accept self as the first param    
    def show_name(self):
        print('This name is {0}'.format(self.name))

    def greet_with(self, greeting):
        print("{0} {1}".format(greeting, self.name))

class Employee(Person):

    def __init__(self, code):
        Person.__init__(self, "")
        self.code = code
    
    def show_code(self):
        print('The code is {0}'.format(self.code))

    def greet_with(self, greeting):
        print('This is from the child class, {} {}'.format(greeting, self.code))

#no new keyword for instance creation
# person = Person("Amar")
# person.show_name()
# person.greet_with("Namaste")

employee = Employee(10)
employee.greet_with("Namaste")

Employee.class_method(2,3)
Employee.static_method(1,2)