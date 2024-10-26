"""
Given the head of a linked list head, in which each node contains an integer
value.

Between every pair of adjacent nodes, insert a new node with a value equal to
the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that
evenly divides both numbers.

Example 1:

Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: The 1st diagram denotes the initial linked list and the 2nd
diagram denotes the linked list after inserting the new nodes (nodes in blue
are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and
the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and
the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and
the 4th nodes.
There are no more adjacent nodes, so we return the linked list.
Example 2:

Input: head = [7]
Output: [7]
Explanation: The 1st diagram denotes the initial linked list and the 2nd
diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.

Constraints:

The number of nodes in the list is in the range [1, 5000].
1 <= Node.val <= 1000
"""
from math import gcd
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def insertGreatestCommonDivisors(
            self,
            head: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Initialize pointers: 'prev_node' pointing to the current node being
        # processed, and 'current_node' pointing to the next node in the list.
        prev_node, current_node = head, head.next

        # Iterate through the linked list until we reach the end.
        while current_node:
            # Compute Greatest Common Divisor (GCD) of the values in the
            # 'prev_node' and 'current_node'.
            gcd_value = gcd(prev_node.val, current_node.val)

            # Insert a new node with the GCD value between the 'prev_node'
            # and 'current_node'.
            prev_node.next = ListNode(gcd_value, current_node)

            # Update pointers: move 'prev_node' to the 'current_node' and
            # 'current_node' to the next node in the list.
            prev_node, current_node = current_node, current_node.next

        # Return the modified linked list head.
        return head
