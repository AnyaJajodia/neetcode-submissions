# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head
        length = 0
        curr=head
        while curr:
            length+=1
            curr = curr.next
        if length<n: return head
        nth = length-n
        count = 0
        if nth == 0: return head.next
        prev=None
        curr=head
        while count!=nth:
            count+=1
            prev=curr
            curr=curr.next
        prev.next=curr.next
        return head
        
        
            
        