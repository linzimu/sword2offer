# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.ans = 0

    def _sum(self, n):
        self.ans += n
        n -= 1
        return n > 0 and self.Sum_Solution(n)

    def Sum_Solution(self, n):
        # write code here
        self._sum(n)
        return self.ans
