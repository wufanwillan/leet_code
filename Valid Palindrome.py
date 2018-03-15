# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome.

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s=="":
            return True
        s=s.lower()
        i,j=0,len(s)-1
        left,right=s[0],s[-1]
        while i<j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            elif not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
        return True
