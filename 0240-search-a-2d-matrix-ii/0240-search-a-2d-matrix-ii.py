class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix),len(matrix[0])

        for i in range(n):
            l = 0
            r = m-1
            while l<=r:
                mid = (l+r)//2
                
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid]>target:
                    r = mid-1
                else:
                    l = mid+1
        return False