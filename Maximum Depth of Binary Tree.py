# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        count=1
        deque1=collections.deque([root])
        deque2=collections.deque([])
        while True:
            while True:
                root=deque1.pop()
                
                if root.left or root.right:
                    if root.left:
                        deque2.append(root.left)
                    if root.right:
                        deque2.append(root.right)
                if not deque1:
                    break
            if deque2:
                count+=1
                deque1,deque2=deque2,deque1
            else:
                break
        return count
