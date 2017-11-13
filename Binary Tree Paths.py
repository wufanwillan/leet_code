# Given a binary tree, return all root-to-leaf paths.

# For example, given the following binary tree:

#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:

# ["1->2->5", "1->3"]
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        result,path=[],[]
        
        def depth(node,path,result):
            if not node:
                return
            
            path.append(str(node.val))
            
            if not (node.left or node.right):
                pathlist="->".join(path)
                result.append(pathlist)
                
            if node.left:
                depth(node.left,path,result)
                path.pop()
                
            if node.right:
                depth(node.right,path,result)
                path.pop()
                
        depth(root,path,result)
        
        return result
