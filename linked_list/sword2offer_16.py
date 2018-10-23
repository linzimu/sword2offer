class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        p_merge = None
        if pHead1.val < pHead2.val:
            p_merge = pHead1
            p_merge.next = self.Merge(pHead1.next, pHead2)
        else:
            p_merge = pHead2
            p_merge.next = self.Merge(pHead1, pHead2.next)
        return p_merge


if __name__ == '__main__':
    p1 = ListNode(1)
    p = p1
    for i in range(3, 11, 2):
        node = ListNode(i)
        p.next = node
        p = node

    p2 = ListNode(2)
    p = p2
    for i in range(4, 11, 2):
        node = ListNode(i)
        p.next = node
        p = node

    p_merge = Solution().Merge(p1, p2)
    p = p_merge
    while p:
        print(p.val, end='\t')
        p = p.next
