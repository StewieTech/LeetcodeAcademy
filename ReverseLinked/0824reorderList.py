from typing import Optional


class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val;
        self.next = next;
    
    def __str__(self):
        result = [];
        current = self;
        while (current):
            result.append(str(current.val));
            current = current.next;
        return "->".join(result);

class Solution:
    def reorderList(self, head: Optional[ListNode] ) -> None:
        slow, fast = head, head.next
        while (fast and fast.next):
            slow, fast = slow.next, fast.next.next;

        second = slow.next;
        prev = slow.next = None;
        while (second):
            second.next, prev, second = prev, second, second.next;
        
        first, second = head, prev;
        while (second):
            first.next, first = second , first.next;
            second.next, second =  first, second.next;

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         if not head:
#             return
        
#         # Find the middle of the linked list
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         # Reverse the second half of the linked list
#         second = slow.next
#         prev = slow.next = None
#         while second:
#             second.next, prev, second = prev, second, second.next
        
#         # Merge the two halves
#         first, second = head, prev
#         while second:
#             first.next, first = second, first.next
#             second.next, second = first, second.next

def main():
    head = ListNode(0);
    head.next = ListNode(1);
    head.next.next = ListNode(2);
    head.next.next.next = ListNode(3);
    head.next.next.next.next= ListNode(4);
    head.next.next.next.next.next= ListNode(5);
    head.next.next.next.next.next.next= ListNode(6);

    Solution().reorderList(head)
    print(head);

    # print(Solution().reorderList(head))

if __name__ == "__main__":
    main();
    
