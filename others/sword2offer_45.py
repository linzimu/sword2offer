# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers.sort()
        zero_nums = numbers.count(0)
        i = zero_nums
        j = i + 1
        gaps = 0
        while j < len(numbers):
            if numbers[i] == numbers[j]:
                return False
            gaps += numbers[j] - numbers[i] - 1
            i, j = j, j + 1
        return gaps <= zero_nums
