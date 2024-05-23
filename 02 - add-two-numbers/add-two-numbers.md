# Add Two Numbers

## Problem Description
<p>You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The digits are stored in <strong>reverse order</strong>, and each of their nodes contains a single digit. Add the two numbers and return the sum&nbsp;as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" />
<pre>
<strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,0,8]
<strong>Explanation:</strong> 342 + 465 = 807.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>Output:</strong> [8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
</ul>

## Solution
```
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper functions
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

# Solution 
def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    sum_number = make_number(l1) + make_number(l2)
    l3 = make_linked_list(sum_number)
    return l3
        
```

## Optimized Solution
```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    # Initialize a dummy node to act as the head of the result linked list.
    dummy = ListNode()
    # 'current' will point to the last node in the result linked list.
    current = dummy
    # 'carry' will store the carry-over value when the sum of two digits exceeds 9.
    carry = 0

    # Loop through both linked lists until both are fully traversed.
    while l1 or l2 or carry:
        # If l1 is not None, get its value, otherwise use 0.
        val1 = l1.val if l1 else 0
        # If l2 is not None, get its value, otherwise use 0.
        val2 = l2.val if l2 else 0

        # Calculate the sum of the two values and the carry.
        total = val1 + val2 + carry
        # Update the carry for the next iteration.
        carry = total // 10
        # Create a new node with the digit value of the total sum mod 10.
        current.next = ListNode(total % 10)
        # Move the current pointer to the newly created node.
        current = current.next

        # Move to the next nodes in l1 and l2, if they exist.
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # The first node of the result linked list is dummy.next.
    return dummy.next
```

## What I Learned
My initial solution was a literal transcription of how I thought about the problem: convert each linked list into an integer, add the integers, and then convert the result back into a linked list. This involved multiple conversions between data types, which is inefficient in terms of both time and memory usage.

The optimized solution, on the other hand, minimizes these conversions. It processes the linked lists directly and uses a carry variable to handle digit sums that exceed 9, similar to how we manually add numbers in grade school. This approach is more efficient and elegant, directly operating on the linked lists and reducing the overall complexity of the code.
