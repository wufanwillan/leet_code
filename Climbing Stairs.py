# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import factorial as mf
        
        cache={}
        
        def comb(m,n):
            def _comb(num):
                if num not in cache.keys():
                    cache[num]=mf(num)
                return cache[num]
                    
            return _comb(m)/_comb(n)/_comb(m-n)
        
        result=0
        count=0
        while n>=count:
            result+=comb(n,count)
            n-=1
            count+=1
