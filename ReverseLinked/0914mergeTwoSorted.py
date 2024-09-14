from typing import Optional


class ListNode:
    def __init__(self, val =0, next = None):
        self.val = val;
        self.next= next;

    def __str__(self) -> str:
        result = [];
        curr = self;
        while (curr) :
            result.append(str(curr.val));
            curr = curr.next();
        return "-> ".join(result);





class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(); 
        curr = dummy;
        while (list1 and list2):
            if list1.val < list2.val:
                curr.next = list1;
                list1 = list1.next;
            else :
                curr.next = list2;
                list2 = list2.next
            curr = curr.next ;
        curr = list1 or list2;
        return dummy.next ;

lst1 = ListNode(1);
lst1 = ListNode(2);
lst2 = ListNode(1);
lst2 = ListNode(3);
print(Solution().mergeTwoLists(lst1, lst2));


