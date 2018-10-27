class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        # 在前面的序列中，找到第一个比根节点大的位置i
        for i in range(len(sequence)):
            if sequence[i] > root:
                break
        # 从位置i到位置len(squence)-1的所有元素都比根节点的值大
        # 否则不符合二叉搜索树
        for j in range(i, len(sequence) - 1):
            if sequence[j] < root:
                return False
        left, right = True, True
        if len(sequence[0:i]) > 0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        if len(sequence[i:-1]) > 0:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right
