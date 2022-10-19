# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
        
    head = ListNode(0)
    cur_node = head

    carry = 0

    while l1 != None or l2 != None or carry != 0:
        
        if l1 != None:
            l1_cur_val = l1.val
        else: 
            l1_cur_val = 0

        if l2 != None:
            l2_cur_val = l2.val
        else:
            l2_cur_val = 0

        column_sum = l1_cur_val + l2_cur_val + carry

        carry = column_sum // 10

        new_node = ListNode(column_sum % 10)
        cur_node.next = new_node
        cur_node = new_node

        if l1 != None:
            l1 = l1.next
        else:
            l1 = None
        
        if l2 != None:
            l2 = l2.next
        else:
            l2 = None
    return head.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

node = addTwoNumbers(l1, l2)

while node != None:
    print(node.val)
    node = node.next