class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        n = len(matrix)
        m = len(matrix[0])

        def util(i,j):
            if(i>=n or j>=m):
                return 0
        
            right = util(i, j+1)
            down = util(i+1, j)
            diag = util(i+1, j+1)

            if(matrix[i][j] == '0'):
                return 0

            return 1 + min(right,down,diag)
        
        max_side = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':  
                    max_side = max(max_side, util(i, j))

        return max_side ** 2


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        n = len(matrix)
        m = len(matrix[0])
        cache = {}

        def util(i,j):
            if(i>=n or j>=m):
                return 0
            
            if((i,j) not in cache):
                right = util(i, j+1)
                down = util(i+1, j)
                diag = util(i+1, j+1)

                cache[(i,j)] = 0
                if(matrix[i][j] == '1'):
                    cache[(i,j)] = 1 + min(right,down,diag)

            return cache[(i,j)]
        
        util(0,0)
        res = max(cache.values())
        return res ** 2