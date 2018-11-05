# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        s = s.strip()
        if not s:
            return 0
        if s[0] == '-':
            return -1 * self._StrToInt(s[1:])
        elif s[0] == '+':
            return self._StrToInt(s[1:])
        else:
            return self._StrToInt(s)

    def _StrToInt(self, s):
        if not s:
            return 0
        ans = 0
        for item in s:
            if '0' <= item <= '9':
                ans = ans * 10 + ord(item) - ord('0')
            else:
                return 0
        return ans
