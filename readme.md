# LeetCode Problems

https://app.codingrooms.com/app/org/bptn-bootcamps-Wikw6pa/course/full-stack-developer-bootcamp%253A-cohort-2-3p7aTai/b/leetcode-problems-qRJ3BCm|

## Average Salary Excluding the Minimum and Maximum Salary

<h4> Approach and Reasoning behind it </h4>
-
<h4> Algorithm Explanation </h4>
-


## Squares of a Sorted Array
<h4> Approach and Reasoning behind it <h4/>
- 
<h4> Algorithm Explanation </h4>
-

## Missing Number
#### Approach and Reasoning behind it
- Understanding the constraints of the question really helped with edge cases. Since the question would only give unique numbers, a set was not needed. Since the minimum number in the zone was 0 it was easier to no logic was needed to account for this. We also know there will be at least one number missing since 0 is included.
##### Logic of First Solution Attempt
- A solution that seems effective would be to sort the list. once the list is sorted, we could run a for loop. 
- We could compare the arrayIndex of the for loop to another numCounter index the numCounter would simply increase by one each loop. 
- When the currentIndex does not equal the numCounter we simply would return the missing number (being the numCounter)
- 
##### Final Thoughts
- For the most part The initial pseudocode solution ended up working. 
- Turning the Array to an ArrayList was unnecessary but easier to work with, This can definitely be refactored if needed
- One edge case where the final number of the array was the missing number was simply accounted for by just  adding a second return statement near the end of the code


#### Algorithm Explanation
- To find the missing number in an Array from 0...n we are given an area nums. nums Is turned to an ArrayList for ease of use (unnecessary) by adding each number to an ArrayList called finalList using a for loop. The ArrayList is sorted for easy comparison. A for loop is then created where Two indexes are compared, 1) for the sortedList, 2)  numCounter which increments each for loop. When the indexes don't match we know that's the missing number, and we can return numCounter. We also have a second return statement outside the for loop for the case when the missing number is the last number of the array
- Algorithm is O(n) due to the for loop

## Add Two Numbers
#### Approach and Reasoning behind it
-
#### Algorithm Explanation
-

## Merge Two Sorted Lists
<h4> Approach and Reasoning behind it </h4>
##### Logic of First Solution Attempt
- The first idea was literally just adding all elements to a single list, sorting it and then if being finished
- Since this is a LinkedList type data structure the 2nd thought was just creating a Linked List Collection and having them be apart of it
- Since this question requires a List node to be returned it became clear that we would need to custom create a ListNode and then traverse it

##### Logic of Second Solution Attempt
- Currently, the option that seems the most accessible is traversing both list and adding the values to an ArrayList
- once it's in an ArrayList, simply turn the data Structure to a LinkedList and return the first number. 
- If we have to use a ListNode custom data structure, then turn each number in the ArrayList to a ListNode, and connect them

#### Algorithm Explanation
- Two lists that are both lists of ListNodes are required to merged together and return a final merged ListNode lists that's sorted. Each ListNode List is turned into an ArrayList (unnessary but easier to manage) and then added to the final merged arrayList. The List is sorted and then turned back into a ListNode List (Not coded yet).