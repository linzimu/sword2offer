# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not popV or len(pushV) != len(popV):
            return False
        _stack = []
        for item in pushV:
            _stack.append(item)
            while _stack and _stack[-1] == popV[0]:
                _stack.pop()
                popV.pop(0)
        if _stack:
            return False
        return True
