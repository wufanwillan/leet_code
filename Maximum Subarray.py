# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=max(nums)
        if c<=0:
            return c
        else:
            maxseq=0
            maxsub=0
            for num in nums:
                maxsub=max(maxsub+num,0)
                maxseq=max(maxseq,maxsub)
            return maxseq
