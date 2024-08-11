package LeetcodeAcademy.MissingNumber;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int missingNumber(int[] nums) {

//        System.out.println(Arrays.sort(nums)) ;
//        Arrays.sort(nums) ;

        // Decided to turn Array into a List to better manage
        List<Integer> finalList = new ArrayList<>();
        Integer numAnswer = 0;
        for (int i= 0; i< nums.length; i++) {
//            System.out.println(i);
            finalList.add(nums[i]);
        }

        // Sorting the list so we can compare it to the correct sequence easier. If the sorted list does not match the expected sequence then I know that's the missing number
        Collections.sort(finalList);
        Integer numCounter = 0;
        for (int i= 0; i < finalList.size()  ; i++) {
            Integer sortedNumber = finalList.get(i);
//            System.out.println(sortedNumber);
//            System.out.println(numCounter);
            if (!sortedNumber.equals(numCounter)) {
                // System.out.print(numCounter);
                numAnswer = numCounter ;
                return numAnswer ;

            }
            numCounter ++ ;

        }

        // if The code reaches this far then we know the the sorted Array matches the expected Counter Array which means that the missing number would be the last number/the list size.
        return finalList.size() ;
    }
}
