# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution and you may not use the same element twice.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(numbers)-1
        result=[]
        
        while i<j:
            sumnum=numbers[i]+numbers[j]
            if sumnum<target:
                i+=1
            elif sumnum>target:
                j-=1
            else:
                result.extend([i+1,j+1])
                break

        return result
