# Description:

# Count the number of prime numbers less than a non-negative number, n.

# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <3:
            return 0
        
        digit=[0]*n
        sq = int(n**0.5)+1
        count=1
        for i in range(3,n,2):
            if not digit[i]:
                count+=1
                if i>sq:
                    continue
                for num in range(i+i,n,i):
                    digit[num]=1
        return count
