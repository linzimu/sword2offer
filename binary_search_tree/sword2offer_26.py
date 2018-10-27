# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.list_head = None
        self.list_tail = None

    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None
        self.Convert(pRootOfTree.left)
        if self.list_head is None:
            self.list_head = pRootOfTree
            self.list_tail = pRootOfTree
        else:
            # 修改双向链表的后指针
            self.list_tail.right = pRootOfTree
            # 修改双向链表的前指针
            pRootOfTree.left = self.list_tail
            # 修改双向链表的尾指针
            self.list_tail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.list_head
