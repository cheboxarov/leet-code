from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        [1,2,3] + [1,5,8] -> [1,1,2,3,5,8]
        """
        if (list1 is None and list2 is None):
            return None
        def get_le(_list1: Optional[ListNode], _list2: Optional[ListNode]):
            if _list1 is None:
                return _list2.val, None, _list2.next
            if _list2 is None:
                return _list1.val, _list1.next, None
            if _list1.val <= _list2.val:
                return _list1.val, _list1.next, _list2
            else:
                return _list2.val, _list1, list2.next

        dummy = ListNode()
        res = dummy
        while list1 or list2:
            el, list1, list2 = get_le(list1, list2)
            res.next = ListNode(el)
            res = res.next

        return dummy.next

list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(1,ListNode(5, ListNode(8)))
result = Solution().mergeTwoLists(list1, list2)

while result is not None:
    print(result.val)
    result = result.next