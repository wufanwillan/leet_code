# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=len(nums)
        
        if total==0:
            return 0
        elif total==1 or total==2:
            return max(nums)
        
        result=[nums[0],nums[1],nums[2]+nums[0]]
        i=3
        while i<total:
            acc=max(result[i-3]+nums[i],result[i-2]+nums[i])
            result.append(acc)
            i+=1
        return max(result[i-1],result[i-2])
