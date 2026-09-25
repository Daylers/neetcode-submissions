class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        list_column = [set() for i in range(len(board))]

        list_3x3 = [[set() for i in range(3)] for j in range(3)]

        for i in range(len(board)):
            set_row = set() 

            for j in range(len(board[i])):
                if board[i][j].isdigit():
                    pass
                else:
                    continue
                
                # int
                if board[i][j] in set_row:
                    return False
                set_row.add(board[i][j])
               
                #column
                if board[i][j] in list_column[j]:
                    return False
                list_column[j].add(board[i][j])

                # 3x3
                x = i // 3
                y = j // 3

                if board[i][j] in list_3x3[x][y]:
                    return False
                list_3x3[x][y].add(board[i][j])
                # print(list_3x3)
        return True