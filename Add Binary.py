# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la=len(a)
        lb=len(b)
        result,car,val=[],0,0
        maxl=max(la,lb)
        for i in range(maxl):
            val=car
            if i<len(a):
                val+=int(a[-(i+1)])
            if i<len(b):
                val+=int(b[-(i+1)])
            car,val=val//2,val%2
            result.append(str(val))
        if car:
            result.append(str(car))
        return ''.join(reversed(result))
