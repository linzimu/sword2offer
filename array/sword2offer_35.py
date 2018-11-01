# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        temp = data[:]
        return self.mergeSort(temp, data, 0, len(data) - 1) % 1000000007

    def mergeSort(self, temp, data, low, high):
        if low >= high:
            return 0
        mid = (low + high) // 2
        left = self.mergeSort(data, temp, low, mid)
        right = self.mergeSort(data, temp, mid + 1, high)

        count = 0
        i = low
        j = mid + 1
        index = low
        while i <= mid and j <= high:
            if data[i] <= data[j]:
                temp[index] = data[i]
                i += 1
            else:
                temp[index] = data[j]
                count += mid - i + 1
                j += 1
            index += 1
        if i <= mid:
            temp[index:index + (mid - i + 1)] = data[i:mid + 1]
        if j <= high:
            temp[index:index + (high - j + 1)] = data[j:high + 1]
        return count + left + right
