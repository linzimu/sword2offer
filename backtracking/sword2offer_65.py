# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        tmp = [True] * rows * cols
        for i in range(rows):
            for j in range(cols):
                if self.find(matrix, rows, cols, i, j, path, tmp):
                    return True
        return False

    def find(self, matrix, rows, cols, i, j, path, tmp):
        if not path:
            return True
        index = i * cols + j
        if i < 0 or i >= rows or j < 0 or j >= cols \
                or matrix[index] != path[0] or not tmp[index]:
            return False
        tmp[index] = False
        if self.find(matrix, rows, cols, i + 1, j, path[1:], tmp) \
                or self.find(matrix, rows, cols, i - 1, j, path[1:], tmp) \
                or self.find(matrix, rows, cols, i, j - 1, path[1:], tmp) \
                or self.find(matrix, rows, cols, i, j + 1, path[1:], tmp):
            return True
        tmp[index] = True
        return False
