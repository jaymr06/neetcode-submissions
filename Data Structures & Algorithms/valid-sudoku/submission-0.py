class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenCols = {i:[] for i in range(9)}
        seenBoxes = {i:[] for i in range(9)}
        for row, rowIndex in zip(board, range(9)):
            seenRow = []
            for i in range(9):
                if row[i] == ".":
                    continue
                    
                if row[i] not in seenRow: # row check
                    seenRow.append(row[i])
                else:
                    return False
                
                if row[i] not in seenCols[i]: # col check
                    seenCols[i].append(row[i])
                else:
                    return False
                
                currBox = rowIndex // 3 * 3 + i // 3
                if row[i] not in seenBoxes[currBox]:
                    seenBoxes[currBox].append(row[i])
                else:
                    return False
        return True
                    

                    
                    
                    

        