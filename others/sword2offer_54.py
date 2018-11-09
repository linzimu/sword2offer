# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self._dict = {}

    def FirstAppearingOnce(self):
        # write code here
        for item in self.s:
            if self._dict[item] == 1:
                return item
        return '#'

    def Insert(self, char):
        # write code here
        self.s = self.s + char
        if char not in self._dict:
            self._dict[char] = 1
        else:
            self._dict[char] = self._dict[char] + 1
