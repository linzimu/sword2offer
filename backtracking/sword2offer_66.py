# -*- coding:utf-8 -*-
class Solution:
    def judge(self, threshold, i, j):
        # 计算i,j中每个数字的总和，并判断是否大于阈值
        if sum(map(int, str(i) + str(j))) <= threshold:
            return True
        else:
            return False

    def findgrid(self, threshold, rows, cols, matrix, i, j):
        # write code here
        count = 0
        if 0 <= i < rows and 0 <= j < cols and \
                self.judge(threshold, i, j) and matrix[i][j] == 0:
            matrix[i][j] = 1  # 标记已经走过的格子
            count = 1 + self.findgrid(threshold, rows, cols, matrix, i, j + 1) \
                    + self.findgrid(threshold, rows, cols, matrix, i, j - 1) \
                    + self.findgrid(threshold, rows, cols, matrix, i + 1, j) \
                    + self.findgrid(threshold, rows, cols, matrix, i - 1, j)
        return count

    def movingCount(self, threshold, rows, cols):
        # matrix记录遍历的格子
        matrix = [[0 for i in range(cols)] for j in range(rows)]
        count = self.findgrid(threshold, rows, cols, matrix, 0, 0)
        return count
