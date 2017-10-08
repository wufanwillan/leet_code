# Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

# Note:

# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly.
# Example 1:

# Input:
# 26

# Output:
# "1a"
# Example 2:

# Input:
# -1

# Output:
# "ffffffff"

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        if num<0:
            flag=-1
            num=pow(2,32)+num
        else:
            flag=1

        index = {i : s for i, s in enumerate("0123456789abcdef")}
        result=[]
        while num > 0:
            res = num % 16
            num//=16
            result.append(index[res])
        result.reverse()

        return ''.join(result)
