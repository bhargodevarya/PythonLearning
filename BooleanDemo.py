# create boolean value
flag = False

def func():
    itr = 1
    '''
    Declaring flag in the global context instead of here creates an error as it is in global context
    and when we try to access set the value it creates an error.
    UnboundLocalError: local variable referenced before assignment

    Mark the flag as global

    Simple usage is fine but use in any expression will cause an error
    '''
    global flag

    while(flag):
        print("Flag is true, will set as false after 5 iterations.")
        if (itr == 5):
            flag = False
        itr += 1

    if (flag):
        print("The flag is true")
    else:
        print("The flag is false")

def simple_use_without_an_expr():
    print(flag)

letter = ""

def calculate_grade(grade):
    global letter
    if grade > 80:
        letter = "A"
    elif grade > 70:
        letter = "B"
    elif grade > 60:
        letter = "C"
    elif grade > 50:
        letter = "D"
    return letter

print(calculate_grade(90))

letter = "random"

print(letter)

func()

simple_use_without_an_expr()