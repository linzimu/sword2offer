# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        p = 0
        q = len(rotateArray) - 1
        mid = p
        while rotateArray[p] >= rotateArray[q]:
            if q - p == 1:
                mid = q
                break
            mid = (p + q) / 2
            if rotateArray[p] == rotateArray[q] and rotateArray[p] == rotateArray[mid]:
                return self.min(rotateArray[p: q])
            if  rotateArray[p] <= rotateArray[mid]:
                p = mid
            elif rotateArray[mid] <= rotateArray[q]:
                q = mid
        return rotateArray[mid]
