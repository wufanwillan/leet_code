# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

# Example:
# Input:
# [[0,0],[1,0],[2,0]]

# Output:
# 2

# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        from collections import Counter
        result=0
        for i,a in enumerate(points):
            distance=[]
            for j,b in enumerate(points):
                if i==j:
                    continue
                distance.append((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)       
            for val in Counter(distance).values():
                if val>1:
                    result+=val*(val-1)
        return result
        
