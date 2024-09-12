from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None) :
        self.val = val;
        self.next = next;

    def __str__(self) -> str:
        result = [];
        current = self;
        while (current) :
            result.append(str(current.val));
            current = current.next;
        return "-> ".join(result);

"""
if we have two lists and we want to put them in sorted order
we are probably using a comparison if operations to know what comes next
if there the same will just default and take the first list
when one list is finished we will just append the rest to the result
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0);
        current = dummy;
        while (list1 and list2) :
            if (list1.val < list2.val):
                current.next = list1; 
                list1 = list1.next ;
            else  :
                current.next = list2 ;
                list2 = list2.next ;
            current = current.next;
        current.next = list1 or list2 ;
        return dummy.next ;

lst1 = ListNode(1);
lst1.next = ListNode(2);
lst1.next.next = ListNode(4);
lst2 = ListNode(1);
lst2.next = ListNode(3);
lst2.next.next = ListNode(5);
print(Solution().mergeTwoLists(lst1,lst2));

        