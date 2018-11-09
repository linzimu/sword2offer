# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        i, j = 0, len(array) - 1
        while i < j:
            _sum = array[i] + array[j]
            # 如果和大于tsum，选择较大数字前面的数字
            if _sum > tsum:
                j -= 1
            # 如果和小于tsum，选择较小数字后面的数字
            elif _sum < tsum:
                i += 1
            else:
                return [array[i], array[j]]
        return []
