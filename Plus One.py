# a.pop(0)Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

# You may assume the integer do not contain any leading zero, except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp=[0]
        temp.extend(digits)
        ln=len(temp)
        
        for i in range(1,ln+1):
            if temp[ln-i]+1<10:
                temp[ln-i]+=1
                break
            temp[ln-i]=0
            
        if temp[0]==0:
            temp.pop(0)
            
        return temp
