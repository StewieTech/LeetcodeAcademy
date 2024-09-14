from typing import Optional


class ListNode:
    def __init__ (self, val=0, next = None):
        self.val = val;
        self.next = next;

    def __str__(self) -> str:
        result = [];
        current = self;
        while (current):
            result.append(str(current.val));
            current = current.next;
        return "-> ".join(result);

    """
    It's as if I am choosing the first item in the list and then after I am choosing the last item in the list
    this makes me feel if I break the list in two and then iterate untill they meet eachother I will be able to solve the question
    """
class Solution:
    # def reorderList(self, head: Optional[ListNode]) -> None:
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast slow
        
        slow = head;
        fast =  head.next
        while ( fast and fast.next ) :
            slow, fast = slow.next, fast.next.next;

        second = slow.next ;
        slow.next = None;
        prev = slow.next;

        # reversing the second half of the list
        while (second) :
            second.next, prev, second = prev, second, second.next ;

        first = head ;
        second = prev ; 
        while (second) :
                first.next , first = second , first.next;
                second.next, second = first, second.next ;
        return head ;
                
head = ListNode(0);
head.next = ListNode(1);
head.next.next = ListNode(2);
head.next.next.next = ListNode(3);
head.next.next.next.next = ListNode(4);
head.next.next.next.next.next = ListNode(5);
head.next.next.next.next.next.next = ListNode(6);

print(Solution().reorderList(head))




            
