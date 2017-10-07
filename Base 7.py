# Given an integer, return its base 7 string representation.

# Example 1:
# Input: 100
# Output: "202"
# Example 2:
# Input: -7
# Output: "-10"
# Note: The input will be in range of [-1e7, 1e7].

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        result=0
        index=0
        if num<0:
            flag=-1
        else:
            flag=1
        num=abs(num)
        while num:
            res=num%7
            result+=res*pow(10,index)
            num/=7
            index+=1
        return str(flag*result)
