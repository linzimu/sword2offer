# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        ans = {}
        for item in s:
            ans[item] = 1 if item not in ans else ans[item] + 1
        for i in range(len(s)):
            if ans[s[i]] == 1:
                return i
        return -1
