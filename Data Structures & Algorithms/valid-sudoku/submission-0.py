class Solution: 
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        list_column = [set() for i in range(len(board))]
        list_3x3 = [[set() for i in range(3)] for j in range(3)]

        m = 0
        k = 0
        x = 0

        for i in range(len(board)):
            set_row = set()
            k = 0
            y = 0                      
            if m == 3:
                m = 0
                x += 1  
            m += 1        

            for j in range(len(board[i])):
                # int

                if board[i][j] in set_row:
                    return False
                if board[i][j].isdigit():
                    set_row.add(board[i][j])
               
                #column
                if board[i][j] in list_column[j]:
                    return False
                if board[i][j].isdigit():             
                    list_column[j].add(board[i][j])

                # 3x3
                if k == 3:
                    k = 0
                    y += 1
                if board[i][j] in list_3x3[x][y]:
                    return False
                if board[i][j].isdigit():             
                    list_3x3[x][y].add(board[i][j])                
                k += 1
        return True