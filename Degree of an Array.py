# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
# Note:

# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        lookup=defaultdict(lambda:0)
        ln=len(nums)
        if ln==1:
            return 1
        for i in range(ln):
            if lookup[nums[i]]:
                lookup[nums[i]][0]+=1
                lookup[nums[i]][1]=i
            else:
                lookup[nums[i]]=[1,i,i]
                
        from functools import reduce
        res=0
        def my_sort(x,y):
            if x[0]>y[0]:
                return x
            elif x[0]==y[0]:
                if y[1]-y[2]<x[1]-x[2]:
                    return y
                else:
                    return x
            else:
                res=y[1]-y[2]
                return y
        num,start,end=reduce(my_sort,lookup.values())
        return start-end+1
