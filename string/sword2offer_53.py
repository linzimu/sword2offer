# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        is_dot, is_e = True, True
        for i in range(len(s)):
            if s[i] in '+-' \
                    and (i == 0 or s[i - 1] in 'eE') \
                    and i < len(s) - 1:
                continue
            elif is_dot and s[i] == '.':
                is_dot = False
                if i == len(s) - 1:
                    return False
            elif is_e and s[i] in 'eE':
                is_dot = False
                is_e = False
                if i == len(s) - 1:
                    return False
            elif s[i] not in '0123456789':
                return False
        return True
