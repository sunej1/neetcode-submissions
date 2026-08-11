class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for row in range(len(matrix)//2):
            temp = matrix[row]
            matrix[row] = matrix[len(matrix)-row-1]
            matrix[len(matrix)-row-1] = temp
        for row in range(len(matrix)):
            for col in range(row):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp


