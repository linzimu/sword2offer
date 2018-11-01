class Solution:
    def GetNumberOfK(self, data, k):
        left = 0
        right = len(data) - 1
        left_k = self.get_left(data, k, left, right)
        right_k = self.get_right(data, k, left, right)
        return right_k - left_k + 1

    def get_left(self, data, k, left, right):
        while left <= right:
            mid = (left + right) // 2
            if data[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def get_right(self, data, k, left, right):
        while left <= right:
            mid = (left + right) // 2
            if k < data[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return right
