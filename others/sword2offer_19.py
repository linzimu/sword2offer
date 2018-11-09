# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        ans = []
        while matrix:
            ans += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return ans

    def turn(self, matrix):
        return map(list, zip(*matrix))[::-1]
