# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        # 当指数为0，指数为负数时
        if base == 0 and exponent < 0:
            return 0
        # 当指数小于0时
        if exponent < 0:
            ans = self._pow(base, -exponent)
            return 1 / ans
        else:
            return self._pow(base, exponent)

    def _pow(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        ans = self._pow(base, exponent >> 1)
        ans *= ans
        if exponent & 1 == 1:
            ans *= base
        return ans
