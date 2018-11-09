# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        ans, factor = 0, 1
        while n / factor != 0:
            low_num = n % factor
            cur_num = (n // factor) % 10
            high_num = n // (factor * 10)
            # 当前位数字为0，则高位数字×当前数字
            if cur_num == 0:
                ans += high_num * factor
            # 当前位数字为1，则高位数字×当前数字 + 低位数字 + 1
            elif cur_num == 1:
                ans += high_num * factor + low_num + 1
            # 当前位数字大于1，则（高位数字+1）×当前数字
            else:
                ans += (high_num + 1) * factor
            factor *= 10
        return ans
