# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k <= 0:
            return None
        ans = []
        self.inOrder(pRoot, ans)
        if len(ans) < k:
            return None
        return ans[k - 1]

    def inOrder(self, root, ans):
        if not root:
            return None
        # 中序遍历
        if root.left:
            self.inOrder(root.left, ans)
        ans.append(root)
        if root.right:
            self.inOrder(root.right, ans)
