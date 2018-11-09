# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        i, j = 1, 2
        _len = (tsum + 1) // 2
        _sum = i + j
        ans = []
        while i < _len:
            if _sum == tsum:
                ans.append(range(i, j + 1))
            while _sum > tsum and i < _len:
                _sum -= i
                i += 1
                if _sum == tsum:
                    ans.append(range(i, j + 1))
            j += 1
            _sum += j
        return ans
