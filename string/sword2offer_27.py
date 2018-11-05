# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) <= 1:
            return ss
        ans = []
        for i in range(len(ss)):
            for item in map(lambda x: ss[i] + x, self.Permutation(ss[:i] + ss[i + 1:])):
                if item not in ans:
                    ans.append(item)
        return ans
