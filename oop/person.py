class Person:

    this_is_a_static_variable = "static variable"

    #constructor
    #self is "this" and should be the first param
    def __init__(self, name="default", age=18):
        self.name = name
        # if a field starts with an _ it means that it should not be touched outside the class
        self._age = age

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
        #Person.__init__(self, "")
        #To call the methods of the super class we can use either the commented 
        #code above or use the super keyword
        super().__init__()
        self.code = code
    
    def show_code(self):
        print('The code is {0}'.format(self.code))

    def greet_with(self, greeting):
        #Calling the parent class methos with the same name
        super().greet_with(greeting)
        print('This is from the child class, {} {}'.format(greeting, self.code))

    #Dunder methods, special methods
    #toString
    def __str__(self):
        return f'code is {self.code}'
    
    def __eq__(self, other):
        return self.code == other.code

    def __call__(self, name):
        print(f'The name is {name}')



#no new keyword for instance creation
# person = Person("Amar")
# person.show_name()
# person.greet_with("Namaste")

employee = Employee(10)
employee.greet_with("Namaste")

print(str(employee))

print(employee == Employee(890))

employee("Magic")