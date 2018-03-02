# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

# Example 1:
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Target = 9

# Output: True
# Example 2:
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Target = 28

# Output: False

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root:
            result=[]
            def presearch(root):
                if root:
                    presearch(root.left)
                    result.append(root.val)
                    presearch(root.right)
                return
            presearch(root)
            print(result)
            lr=len(result)
            curr1,curr2=0,lr-1
            while curr1!=curr2:
                sumre=result[curr1]+result[curr2]
                if sumre>k:
                    curr2-=1
                elif sumre<k:
                    curr1+=1
                else:
                    return True
        return False
