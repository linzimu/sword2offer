# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        ans, times = 0, 0
        for item in numbers:
            # 如果times为0，则把下一个元素赋值给ans，并将次数设为0
            if times == 0:
                ans = item
                times = 1
            # 如果ans与下一个元素的值相等，则将items的次数加1
            elif ans == item:
                times += 1
            # 如果ans与下一个元素的值不相等，则将times的次数减1
            else:
                times -= 1
        return ans if numbers.count(ans) * 2 > len(numbers) else 0
