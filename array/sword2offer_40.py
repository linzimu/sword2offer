class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        xor = 0
        for item in array:
            xor ^= item
        mark = 1
        while xor & mark == 0:
            mark <<= 1
        num1, num2 = 0, 0
        for item in array:
            if item & mark == 0:
                num1 ^= item
            else:
                num2 ^= item
        return num1, num2
