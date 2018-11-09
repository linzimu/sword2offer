# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            _sum = num1 ^ num2
            carray = (num1 & num2) << 1
            num1 = _sum & 0xffffffff
            num2 = carray
        return num1 if num1 >> 31 == 0 else num1 - 2 ** 32
