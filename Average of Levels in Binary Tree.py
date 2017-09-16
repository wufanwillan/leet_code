# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
# The range of node's value is in the range of 32-bit signed integer.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return None
        result=[]
        deque1=collections.deque([])
        deque2=collections.deque([])
        result.append(root.val)
        deque1.append(root)
        while True:
            count=0
            sumn=0
            while deque1:
                root=deque1.popleft()
                if root.left:
                    deque2.append(root.left)
                    sumn+=root.left.val
                    count+=1
                if root.right:
                    deque2.append(root.right)
                    sumn+=root.right.val
                    count+=1
            if count<>0:
                result.append(sumn/(count*1.0))            
                deque1,deque2=deque2,deque1
            else:
                break
        return result
