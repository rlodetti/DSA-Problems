# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def make_number(linked_list):
        number = 0
        scaler = 1
        current_node = linked_list
        while current_node:
            number += current_node.val*scaler
            scaler *= 10
            current_node = current_node.next
        return number
    
def make_linked_list(number):
    number_str = str(number)[::-1]
    head = ListNode(number_str[0])
    current = head
    for val in number_str[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_number = make_number(l1) + make_number(l2)
        l3 = make_linked_list(sum_number)
        return l3
        
    