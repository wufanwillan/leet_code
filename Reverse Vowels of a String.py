# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:
# Given s = "hello", return "holle".

# Example 2:
# Given s = "leetcode", return "leotcede".

# Note:
# The vowels does not include the letter "y".
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        vowels=set("aeiouAEIOU")       
        s=list(s)
        pointer1=0
        pointer2=len(s)-1
        while True:
            while pointer1<pointer2 and s[pointer1] not in vowels:
                pointer1+=1
            while pointer1<pointer2 and s[pointer2] not in vowels:
                pointer2-=1
            if pointer1==pointer2 or pointer1>pointer2:
                break
            else:
                s[pointer1],s[pointer2]=s[pointer2],s[pointer1]
                pointer1+=1
                pointer2-=1
        return ''.join(s)
