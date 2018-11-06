# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number < 3:
            return number
        ans = 1
        for _ in range(2, number + 1):
            ans *= 2
        return ans
