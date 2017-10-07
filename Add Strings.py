# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def tr(num):
            return ord(num)-ord('0')
        l1=list(reversed(list(num1)))
        l2=list(reversed(list(num2)))
        minl=min(len(num1),len(num2))
        carry=0
        result=[]
        for index in range(minl):
            total=tr(l1[index])+tr(l2[index])+carry
            result.append(total%10)
            carry=total/10
        if len(num1)>len(num2):
            for index2 in range(len(num1)-minl):
                total=tr(l1[index2+index+1])+carry
                result.append(total%10)
                carry=total/10
        else:
            for index2 in range(len(num2)-minl):
                total=tr(l2[index2+index+1])+carry
                result.append(total%10)
                carry=total/10
        if carry>0:
            result.append(carry)
        result.reverse()
        return ''.join(map(str,result))
