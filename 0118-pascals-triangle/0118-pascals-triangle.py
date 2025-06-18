class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        
        triangle = []

        for row in range(numRows):
            # Start each row with 1
            current_row = [1] * (row + 1)
            # fill in the values for the current row based on the previous row
            for j in range(1, row):
                current_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]
            # append the current row to the triangle
            triangle.append(current_row)
        return triangle