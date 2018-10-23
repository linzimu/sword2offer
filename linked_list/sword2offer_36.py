class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 is None or pHead2 is None:
            return None
        cur1, cur2 = pHead1, pHead2
        while cur1 != cur2:
            cur1 = cur1.next if cur1 is not None else pHead2
            cur2 = cur2.next if cur2 is not None else pHead1
        return cur1


def create_linked_list(arr=None):
    pHead = ListNode(arr[0])
    p = pHead
    for i in arr[1:]:
        node = ListNode(i)
        p.next = node
        p = node
    return pHead


if __name__ == '__main__':
    # 有问题.测试没有通过
    p1 = create_linked_list(arr=[2, 1, 0])
    # p = p1
    # while p:
    #     print(p.val, end='\t')
    #     p = p.next
    # print()
    p2 = create_linked_list(arr=[4, 3, 1, 0])
    # p = p2
    # while p:
    #     print(p.val, end='\t')
    #     p = p.next
    # print()
    print(Solution().FindFirstCommonNode(p1, p2))
