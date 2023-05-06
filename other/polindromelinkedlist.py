# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return None
        
        middle = self.middleNode(head)
        reverse = self.reverseList(middle)

        while reverse:
            if reverse.val != head.val:
                return False
            
            reverse = reverse.next
            head = head.next
        return True

        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        return prev

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow    