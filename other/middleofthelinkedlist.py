# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# find the middle element of the linked list
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow