class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        matrix.reverse()
        print(matrix)
        n = len(matrix)

        # 0,0   0,1   0,2
        # 1,0   1,1   1,2
        # 2,0   2,1   2,2

        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                