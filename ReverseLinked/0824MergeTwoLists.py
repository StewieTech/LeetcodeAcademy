from typing import Optional


class ListNode:
    def __init__ (self, val=0, next = None):
        self.val = val;
        self.next = next;

    def __str__ (self):
        result = [];
        current = self;
        while current:
            result.append(str(current.val))
            current = current.next
        return "-> ".join(result);
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0);
        newList = dummy;
        while list1 and list2:
            newList.next, list1, list2 = (list1, list1.next, list2) if (list1.val < list2.val) else (list2, list1, list2.next);
            newList = newList.next;
        newList.next = list1 or list2;
        return dummy.next ;


# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         newList = dummy
        
#         while list1 and list2:
#             if list1.val < list2.val:
#                 newList.next = list1
#                 list1 = list1.next
#             else:
#                 newList.next = list2
#                 list2 = list2.next
#             newList = newList.next
        
#         newList.next = list1 or list2
#         return dummy.next


def main():
    headOne = ListNode(1);
    headOne.next = ListNode(2);
    headOne.next.next = ListNode(4);
    headTwo= ListNode(1);
    headTwo.next = ListNode(3);
    headTwo.next.next = ListNode(5);
    print(Solution().mergeTwoLists(headOne, headTwo))

if __name__ == "__main__":
    main();