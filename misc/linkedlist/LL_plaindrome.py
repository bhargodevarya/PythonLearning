class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


ll_3 = ListNode(3)
ll_1_1 = ListNode(1)
ll_2_1 = ListNode(2)

ll_1_2 = ListNode(1)
ll_2_2 = ListNode(2)

ll_1_1.next = ll_2_1
ll_2_1.next = ll_3

ll_3.next = ll_2_2
ll_2_2.next = ll_1_2

dummy = ll_1_1

gl = 'global'

def is_palindrome(node: ListNode):
    dummy = node
    print(gl)
    return recur(node)

def recur(node: ListNode) :
    if node is None or node.next is None:
        return node
    
    recur_result = recur(node.next)
    if recur_result == False:
        return False
    else:
        res = dummy.val == node.val
        if res:
            dummy = dummy.next
            return True
        else:
            return False

print(is_palindrome(ll_1_1))