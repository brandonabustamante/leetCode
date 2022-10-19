# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dec_pos = 0
    l1_sum = 0
    l2_sum = 0
    tot_sum = 0
    tot_list = ListNode()
    cur_node = tot_list
    
    while l1 != None:
        l1_sum += l1.val * pow(10,dec_pos)
        dec_pos += 1
        l1 = l1.next
    dec_pos = 0
    while l2 != None:
        l2_sum += l2.val * pow(10,dec_pos)
        dec_pos += 1
        l2 = l2.next    
    tot_sum = l1_sum + l2_sum
    
    if tot_sum == 0:
        return tot_list
    while tot_sum != 0:
        new_node = ListNode(tot_sum % 10)
        cur_node.next = new_node
        cur_node = cur_node.next
        tot_sum = tot_sum // 10
    
    return tot_list.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

node = addTwoNumbers(l1, l2)


while node:
    print (node.val)
    node = node.next