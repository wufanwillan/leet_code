# Given an integer, write a function to determine if it is a power of three.

# Follow up:
# Could you do it without using any loop / recursion?

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        from math import log
        maxint=pow(3,int(log(0x7fffffff)/log(3)))
        return maxint%n==0 if n>0 else False
        
