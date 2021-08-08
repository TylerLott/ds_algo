"""
Leetcode 19. remove the Nth node from end of linked list


My idea here is to traverse the whole list and bubble back up to the correct
number using recursion and removing that. Looks like we will need a dummy node
at the beginning as well to take care of edge cases. 

Time complexity O(n) 
space O(n)

This can probably also be done with iteration and no recursion to save space

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n: int):
    dummy = ListNode()
    dummy.next = head
    helper(dummy, n)
    return dummy.next


def helper(self, node, n) -> int:
    if node.next:
        i = self.helper(node.next, n) + 1
    else:
        i = 1
    if i == n + 1:
        node.next = node.next.next
    return i
