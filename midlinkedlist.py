# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        mid = head
        count = 0

        while head:
            if count%2 != 0:
                mid = mid.next
            head = head.next
            count += 1
        return mid
