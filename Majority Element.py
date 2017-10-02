# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c=Counter(nums)
        maxindex=0
        maxval=len(nums)//2
        for index,val in c.items():
            if val > maxval:
                maxindex=index
        return maxindex
