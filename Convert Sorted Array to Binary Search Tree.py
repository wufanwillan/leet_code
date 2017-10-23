# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def pivot(num):
            base=1<<num.bit_length()-1
            if num-(base-1)>=base>>1:
                return base-1
            else:
                return num-base>>1
            
        def sortedat(num,start,end):
            interval=end-start
            if interval<=0:
                return None
            mid=start+pivot(interval)
            node=TreeNode(num[mid])
            node.left=sortedat(num[start:mid],start,mid)
            node.right=sortedat(num[mid+1:end],mid+1,end)
            return node
        
        node=sortedat(nums,0,len(nums))
        return node

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        import math
        ln = len(nums)
        if ln == 0:
            return None
        elif ln==1:
            return TreeNode(nums[0])
        
        tree_depth=int(math.log(ln+1,2))
        complete_length=1>>tree_depth-1
        complete_balance_l=nums[:complete_length]
        leaf_l=nums[complete_length:]
        
        def full_complete_tree(numlist):
            mid=len(numlist)//2
            if mid==0:
                node=TreeNode(numlist[0])
            else:        
                node=TreeNode(numlist[mid])
                node.left=full_complete_tree(numlist[:mid])
                node.right=full_complete_tree(numlist[mid+1:])
            return node
        complete_tree=full_complete_tree(complete_balance_l)
        leaf_l.reverse()
        leaf_warehouse=leaf_l
        
        def full_uncomplete(numlist,node):
            if not node.left:
                if not numlist:
                    return complete_tree
                node.left=TreeNode(numlist.pop())

            if not node.right:
                if not numlist:
                    return complete_tree
                node.right=TreeNode(numlist.pop())
            
            return
                
        def full_uncomplete_tree(numlist,node):
            
            if node.left:
                full_uncomplete_tree(leaf_warehouse,node.left)
            if node.right:
                full_uncomplete_tree(leaf_warehouse,node.right)
            full_uncomplete(leaf_warehouse,node)
            return
                
        full_uncomplete_tree(leaf_warehouse,complete_tree)
        
        return complete_tree
