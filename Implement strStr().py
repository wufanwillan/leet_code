# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def kmp(string,pattern,table):
            if string is None:
                return -1
            ls=len(string)
            lp=len(pattern)
            i,j=0,0
            while i<ls and j<lp:
                if j==-1 or string[i]==pattern[j]:
                    i+=1
                    j+=1
                else:
                    j=table[j]
            if j>=lp:
                return i-j
            else:
                return -1
            
        def gen_table(pattern):
            k=-1
            lp=len(pattern)
            table=[-1]
            i=0
            while i<lp-1:
                if k==-1 or pattern[i]==pattern[k]:
                    k+=1
                    i+=1
                    table.append(k)
                else:
                    k=table[k]
            return table
        
        table=gen_table(needle)
        return kmp(haystack,needle,table)
