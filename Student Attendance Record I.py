# You are given a string representing an attendance record for a student. The record only contains the following three characters:

# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

# You need to return whether the student could be rewarded according to his attendance record.

# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ls=len(s)
        counta=0
        countl=0
        for i in range(ls):
            if s[i]=='A':
                counta+=1
            if s[i]=='L':
                if i+1<ls and i+2<ls:
                    if s[i+1]=='L' and s[i+2]=='L':
                        countl+=1
            if counta>2 or countl>0:
                break
        if counta>1 or countl>0:
            return False
        else:
            return True
