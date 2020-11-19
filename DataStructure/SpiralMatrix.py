class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        result = []
        if len(matrix) == 0:
            return result;
        top = 0;
        bottom = len(matrix)-1;
        left = 0;
        counter = 0
        right = len(matrix[0])-1;
        totalSize = len(matrix) * len(matrix[0]);
        while counter < totalSize:
            for i in range(left, right + 1):
                if counter < totalSize:
                     counter += 1
                     result.append(matrix[top][i]);
            top += 1;
            for i in range(top, bottom + 1):
                if counter < totalSize:
                    counter += 1
                    result.append(matrix[i][right]);
            right -= 1;
            for i in range(right, left-1, -1):
                if counter < totalSize:
                    counter+= 1
                    result.append(matrix[bottom][i]);
            bottom -= 1;
            for i in range(bottom,  top - 1, -1):
                if counter < totalSize:
                    counter += 1
                    result.append(matrix[i][left]);
            left += 1
        return result