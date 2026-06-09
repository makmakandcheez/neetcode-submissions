class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r, row in enumerate(board):
            seen = set()
            for c, num in enumerate(row):
                if num == ".":
                    continue
                elif num in seen:
                    return False
                elif num in columns[c]:
                    return False
                elif num in squares[(r // 3)*3 + c // 3]:
                    return False
                else:
                    seen.add(num)
                    columns[c].add(num)
                    squares[(r // 3)*3 + c // 3].add(num)
        return True
