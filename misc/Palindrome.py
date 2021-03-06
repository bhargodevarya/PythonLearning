def palindrome(string):
    if string is None:
        return False
    
    if len(string) < 2:
        return True
    
    start = 0 
    end = len(string)-1

    while start <= end:
        if string[start] == string[end]:
            start += 1
            end -=1
        else:
            return False
    
    return True

print(palindrome(''))