class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        # 复制节点在原节点之后
        pCur = pHead
        while pCur is not None:
            node = RandomListNode(pCur.label)
            node.next = pCur.next
            pCur.next = node
            pCur = node.next
        # 复制random指针
        pCur = pHead
        while pCur is not None:
            if pCur.random is not None:
                pCur.next.random = pCur.random.next
            pCur = pCur.next.next
        # 将新旧链表分离
        head = pHead.next
        cur = head
        pCur = pHead
        while pCur is not None:
            pCur.next = pCur.next.next
            # 如果不是最后一个节点
            if cur.next is not None:
                cur.next = cur.next.next
            cur = cur.next
            pCur = pCur.next
        return head
