# Write a program to find the node at which the intersection of two singly linked lists begins.


# For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.


# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# Credits:
# Special thanks to @stellari for adding this problem and creating all test cases.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        count1,count2,count=0,0,0
        nodeA,nodeB=headA,headB
        while nodeA:
            count1+=1
            nodeA=nodeA.next
        while nodeB:
            count2+=1
            nodeB=nodeB.next
        
        if count1>count2:
            diff=count1-count2
            while diff:
                diff-=1
                headA=headA.next
        else:
            diff=count2-count1
            while diff:
                diff-=1
                headB=headB.next
                
        while headA and headB and not (headA is headB):
            headA=headA.next
            headB=headB.next
        if headA is headB:
            return headA
        else:
            return False
