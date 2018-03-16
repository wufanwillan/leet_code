# Rotate an array of n elements to the right by k steps.

# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

# [show hint]

# Related problem: Reverse Words in a String II

# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k>0:
            ln=len(nums)
            k=k%ln
            for i in range((ln-k)//2):
                nums[i],nums[ln-k-i-1]=nums[ln-k-i-1],nums[i]
            for i in range(k//2):
                nums[-i-1],nums[-k+i]=nums[-k+i],nums[-i-1]

            for i in range(ln//2):
                nums[i],nums[ln-1-i]=nums[ln-1-i],nums[i]
