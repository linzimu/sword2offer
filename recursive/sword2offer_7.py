# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n < 2:
            return n
        item1, item2, ans = 0, 1, 0
        for _ in range(2, n + 1):
            ans = item1 + item2
            item1 = item2
            item2 = ans
        return ans
