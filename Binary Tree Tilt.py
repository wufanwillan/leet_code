# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def postOrderTraverse(root, tilt):
            if not root:
                return 0, tilt
            left, tilt = postOrderTraverse(root.left, tilt)
            right, tilt = postOrderTraverse(root.right, tilt)
            tilt += abs(left-right)
            return left+right+root.val, tilt

        return postOrderTraverse(root, 0)[1]
