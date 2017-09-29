# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

# Example:

# Input:

#    1
#     \
#      3
#     /
#    2

# Output:
# 1

# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result=[]
        def deeproot(root):
            if root:
                deeproot(root.left)
                result.append(root.val)
                deeproot(root.right)
            return
        deeproot(root)
        diff=[]
        lr=len(result)
        for i in range(lr-1):
            diff.append(result[i+1]-result[i])
        return min(map(lambda x:abs(x),diff))
