# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number < 3:
            return number
        item1, item2, ans = 1, 2, 0
        for _ in range(3, number + 1):
            ans = item1 + item2
            item1 = item2
            item2 = ans
        return ans
