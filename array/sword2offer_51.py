# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return []
        B = [1]
        for i in range(1, len(A)):
            B.append(B[i - 1] * A[i - 1])
        tmp = 1
        for i in range(len(A) - 1)[::-1]:
            tmp *= A[i + 1]
            B[i] *= tmp
        return B
