# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # tmp 表示加上item之后的子数组的最大和
        ans, tmp = -999999, 0
        for item in array:
            if tmp > 0:
                tmp += item
            else:
                tmp = item
            if tmp > ans:
                ans = tmp
        return ans
