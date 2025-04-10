class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix) - 1
        c = len(matrix[0]) - 1
        visited = set()
        res = []
        searching_row = True
        outward = True
        downward = True
        row = 0
        col = 0
        total = (r + 1) * (c + 1)  # ✅ fix: include full matrix size

        while len(res) < total:  # ✅ fix: dynamic based on total
            if (row, col) not in visited:  # ✅ only add if not already visited
                visited.add((row, col))
                res.append(matrix[row][col])

            if searching_row:
                if outward:
                    if col + 1 <= c and (row, col + 1) not in visited:
                        col += 1
                    else:
                        searching_row = False
                        outward = not outward
                        row += 1 if downward else -1
                else:
                    if col - 1 >= 0 and (row, col - 1) not in visited:
                        col -= 1
                    else:
                        searching_row = False
                        outward = not outward
                        row += 1 if downward else -1
            else:
                if downward:
                    if row + 1 <= r and (row + 1, col) not in visited:
                        row += 1
                    else:
                        searching_row = True
                        downward = not downward
                        col -= 1 if not outward else -1
                else:
                    if row - 1 >= 0 and (row - 1, col) not in visited:
                        row -= 1
                    else:
                        searching_row = True
                        downward = not downward
                        col += 1 if outward else 1

        return res