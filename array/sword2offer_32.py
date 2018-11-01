# -*- coding:utf-8 -*-


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numbers = list(map(str, numbers))
        len_num = len(numbers)

        for i in range(len(numbers) - 1):
            for j in range(i + 1, len_num):
                tmp = int(numbers[i] + numbers[j]) - int(numbers[j] + numbers[i])
                if tmp > 0:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return ''.join(numbers)
