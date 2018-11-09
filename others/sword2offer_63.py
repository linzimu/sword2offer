# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.nums = []

    def Insert(self, num):
        # write code here
        self.nums.append(num)
        self.nums.sort()

    def GetMedian(self, nums):
        # write code here
        _len = len(self.nums)
        # 如果是奇数
        if _len % 2 == 1:
            return self.nums[(_len - 1) // 2]
        else:
            return (self.nums[_len // 2] + self.nums[_len // 2 - 1]) / 2.0
