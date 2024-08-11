package LeetcodeAcademy.MergeTwoSortedLists;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.ListIterator;

// This is a created ListNode, each member of the LinkedList is its own ListNode that contains a value and points to the next ListNode
class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }

    // Creating a helper method that adds every value of a list to an ArrayList. The thought is that If we add all ListNodes value's to an ArrayList we can easily sort them.
    // Currently trying to cast ListNode to the entire ArrayList but obviously that won't work, instead will need to create a method that turns all of the ArrayList elements back into ListNodes
    public static ArrayList<Integer> traverseList(ListNode head) {
        ArrayList<Integer> mergedArrayList = new ArrayList<>();
        while (head != null) {
            mergedArrayList.add(head.val);
            System.out.print(head.val +" ");
            head = head.next;
        }
//        return  (ListNode) mergedArrayList;
        return  mergedArrayList;
    }

}

/**
 * Traversing a Linked List
 * <a href="https://www.geeksforgeeks.org/traversal-of-singly-linked-list/">Traversing a Linked List</a>
 *
 */
public class MergeTwoSortedListsDraft {
    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ArrayList<Integer> firstArray = ListNode.traverseList(list1);
        ArrayList<Integer> secondArray = ListNode.traverseList(list2);
        ArrayList<Integer> mergedArray = null;

        // After turning both ListNode Arrays into ArrayLists we add them both to a new Merged Array List
        mergedArray.addAll(firstArray);
        mergedArray.addAll(secondArray);

        // We sort the merged List
        Collections.sort(mergedArray);


        ListNode beforeHead = new ListNode(0);
        ListNode current = beforeHead;

        for (int data : arrayList ) {
           current.next =  mergedArray.get(i);
        }
        return (ListNode) mergedArray; // Need to convert this sorted array into an array of List Nodes


    }
    public static void main(String[] args) {
//        ListNode List1 = [1,2,4] ;
        ListNode list1 = new ListNode(1);
        list1.next = new ListNode(2);
        list1.next.next = new ListNode(4);

//        ListNode List2 = [1,3,4] ;
        ListNode list2 = new ListNode(1);
        list2.next = new ListNode(3);
        list2.next.next = new ListNode(4);

        ListNode Answer = mergeTwoLists(list1,list2);
        System.out.println(Answer);
    }



}

