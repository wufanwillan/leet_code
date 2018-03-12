# Given a singly linked list, determine if it is a palindrome.

# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None:
            return True
        reverse=None
        slow,fast=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow.next,reverse,slow=reverse,slow,slow.next
        tail=slow.next if fast else slow
        while tail:
            if tail.val==reverse.val:
                tail=tail.next
                reverse=reverse.next
            else:
                return False
        return True
