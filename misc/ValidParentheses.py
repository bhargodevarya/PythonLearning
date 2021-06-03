def validate_parentheses(string):
    my_Stack = []

    for item in string:
        if item == '(':
            my_Stack.append('(')
        else:
            if len(my_Stack) == 0:
                return False
            elif my_Stack[len(my_Stack)-1] == '(':
                my_Stack.pop()
            else:
                my_Stack.append(')')
    

    return len(my_Stack) == 0
            
print(validate_parentheses('(()))'))