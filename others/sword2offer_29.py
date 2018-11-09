# -*- coding:utf-8 -*-
import heapq


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        ans = []
        if tinput is None or k < 1 or k > len(tinput):
            return ans
        for item in tinput:
            item = -item
            if len(ans) < k:
                heapq.heappush(ans, item)
            else:
                heapq.heappushpop(ans, item)
        return sorted(map(lambda x: -x, ans))
