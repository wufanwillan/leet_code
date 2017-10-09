# Given an integer, write a function to determine if it is a power of two.

# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>0:
            mask=(1<<(n.bit_length()-1))-1
            return (n&mask)==0
        return False
        
