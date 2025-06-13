# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


from typing import Optional
import operator


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverselink(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def show(head: Optional[ListNode]) -> list[int]:
    curr = head
    links = []
    while curr:
        links.append(curr.val)
        curr = curr.next
    return links


def concat(lst: list[int]) -> int:
    return int("".join(map(str, lst)))


def lastt(lst: list[int]) -> Optional[ListNode]:
    lst.reverse()
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def print_linkedlist(head: Optional[ListNode]):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals))


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1 = reverselink(l1)
        l2 = reverselink(l2)
        k = show(l1)
        l = show(l2)
        a = concat(k)
        b = concat(l)
        c = a + b
        last = list(map(int, str(c)))
        return lastt(last)


# ------------------------
# Example usage:

# Creating l1 = 2 -> 4 -> 3 (which represents 342)
l1 = ListNode(2, ListNode(4, ListNode(3)))

# Creating l2 = 5 -> 6 -> 4 (which represents 465)
l2 = ListNode(5, ListNode(6, ListNode(4)))

sol = Solution()
result = sol.addTwoNumbers(l1, l2)

# Output: 7 -> 0 -> 8 (since 342 + 465 = 807)
print_linkedlist(result)
