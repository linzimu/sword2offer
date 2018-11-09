# -*- coding:utf-8 -*-
from collections import deque


class Solution:
    def maxInWindows(self, num, size):
        # write code here
        ans = []
        if not num or size < 1 or size > len(num):
            return ans
        if size == 1:
            return num
        q = deque()
        q.append(0)
        for i, val in enumerate(num[1:], 1):
            if num[q[-1]] <= val:
                for j in range(len(q) - 1, -1, -1):
                    if num[q[j]] > val:
                        break
                    else:
                        q.pop()
            q.append(i)
            if size <= i - q[0]:
                q.popleft()
            if i >= size - 1:
                ans.append(num[q[0]])
        return ans
