def valid_anagrams(string1, string2):
    if len(string2) != len(string1):
        return False

    my_set = {}
    
    for chars in string1:
        if chars not in my_set.keys():
            my_set[chars] = 1
        else:
            my_set[chars] = my_set[chars]+1
    
    for chars in string2:
        if chars in my_set and my_set[chars] > 0:
            my_set[chars] = my_set[chars]-1
        else:
            return False
    
    return True



    
    
    

