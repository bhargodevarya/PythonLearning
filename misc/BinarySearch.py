
import math

def find(num, my_list):
    if not my_list or len(my_list) == 0:
        return None
    start = 0
    end = len(my_list)-1
    return recur(start, end, my_list, num)

def recur(start, end, my_list, num):
    if start > end or end < start or start < 0 or end >= len(my_list):
        return None
    
    mid = math.floor((start+end)/2)

    if my_list[mid] == num:
        return mid
    
    if num < my_list[mid]:
        return recur(start, mid-1, my_list, num)
    else:
        return recur(mid+1, end, my_list, num)

print(find(11, [1,2,3,4,5,6,7,8,9,10]))