# -*- coding:utf-8 -*-
# 思路：
# (1)只有找到叶子节点并且其值等于指定val时返回
# (2)如果不是叶子节点，分别对其孩子节点进行递归遍历，直到找到叶子节点且其值等于指定val。
# (3)若果没有找到路径，其实也返回了序列，只不过是[]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        # 如果找到叶子节点,同时它的值等于指定的值
        if not root.left and not root.right and expectNumber == root.val:
            return [[root.val]]
        # 不是叶子节点，分别对根节点的子节点进行递归
        ans = []
        left = self.FindPath(root.left, expectNumber - root.val)
        right = self.FindPath(root.right, expectNumber - root.val)
        for item in left + right:
            ans.append([root.val] + item)
        return ans
