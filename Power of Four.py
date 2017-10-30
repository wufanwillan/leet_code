# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example:
# Given num = 16, return true. Given num = 5, return false.

# Follow up: Could you solve it without loops/recursion?
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num>0:
            import math
            if (not (num&num-1)) and (math.log(num,2)%2==0):
                return True
        return False    
