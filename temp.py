class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return False
        
        l=len(matrix)
        for i in range(l):
            matrix[i]=matrix[i:]+matrix[:i]
                
        import numpy as np
        npmatrix=np.array(matrix)
        r,c=npmatrix.shape
        npcl=npmatrix-npmatrix[0]
        if r>c:
            front=npc1[:,:r-c]
            back=npcl[:,r-c:]
        else:
            front=npcl[:c-r,:]
            back=npcl[c-r:,:]
        frontflag=front.any()
        for line in back:
