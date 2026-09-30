class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_len = len(matrix[:])
        max_seen = -1
        for i in range(matrix_len-1,-1,-1):
            
            if matrix[i][0]<=target :
                for j in range(0,len(matrix[i])):                    
                    if matrix[i][j]==target:
                        return True
                        
                
        else:
            return False
          