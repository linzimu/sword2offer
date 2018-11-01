class Solution:
    def duplicate(self, numbers, duplication):
        for i in range(len(numbers)):
            if numbers[i] != i:
                tmp = numbers[numbers[i]]
                if tmp == numbers[i]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    numbers[numbers[i]] = numbers[i]
                    numbers[i] = tmp
        return False
