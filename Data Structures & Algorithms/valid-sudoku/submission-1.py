class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        for i in range(9):
            nums = ["1","2","3","4","5","6","7","8","9"]  
            for j in range(9):
                if board[i][j] in nums:
                    nums.remove(board[i][j])
                elif board[i][j] != ".":
                    return False
          
        for i in range(9):
            nums = ["1","2","3","4","5","6","7","8","9"]  
            for j in range(9):
                if board[j][i] in nums:
                    nums.remove(board[j][i])
                elif board[j][i] != ".":
                    return False

        for i in range(3):
            nums = ["1","2","3","4","5","6","7","8","9"]  
            for j in range(3):
                for k in range(3):
                    if board[j+i*3][k] in nums:
                        nums.remove(board[j+i*3][k])
                    elif board[j+i*3][k] != ".":
                        return False
        
        return True
        