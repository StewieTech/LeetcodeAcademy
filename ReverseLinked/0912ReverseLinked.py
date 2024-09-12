from typing import List, Optional

"""
1 - > 2 -> 3
3-> 2 -> 1
"""

class ListNode:
    def __init__( self, val = 0 , next = None):
        self.val = val;
        self.next = next;
    
    # def __str__(self) -> str:
    def __str__(self) -> str:
        result = [];
        current = self;
        while (current) :
            result.append(str(current.val));
            current = current.next;
        return "-> ".join(result);

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head ;
        prev = None ;
        while (current) :
            # current.next, prev, current = prev, current, current.next;
            temp = current.next;
            current.next = prev;
            prev = current;
            current = temp ;
            return prev

test = ListNode(1,ListNode(2, ListNode(3)));
print(Solution().reverseList(test));
