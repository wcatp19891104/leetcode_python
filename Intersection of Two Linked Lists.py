__author__ = 'wangzaicheng'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        len1 = 1
        len2 = 1
        curr_1 = headA
        curr_2 = headB
        while curr_1.next is not None:
            len1 += 1
            curr_1 = curr_1.next
        while curr_2.next is not None:
            len2 += 1
            curr_2 = curr_2.next
        i = 0
        if len1 < len2:
            while i < (len2 - len1):
                headB = headB.next
                i += 1
        if len1 > len2:
            while i < (len1 - len2):
                headA = headA.next
                i += 1
        while headA is not None and headB is not None:
            if headA.val == headB.val:
                return headA
            headA = headA.next
            headB = headB.next
        return None


if __name__ == "__main__":
    headA = ListNode(3)
    headB = ListNode(2)
    headB.next = ListNode(3)
    s = Solution()
    s.getIntersectionNode(headA, headB)
