package LeetcodeAcademy.MissingNumber;


// Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
public class MissingNumberDraft {

public static void main(String[] args) {
//    missingNumberLeet
    int[] targetArray = {1,2,4,0};
    missingNumber(targetArray) ;
}

    public static void missingNumber(int[] nums) {

//        System.out.println(Arrays.sort(nums)) ;
//        Arrays.sort(nums) ;
        List<Integer> finalList = new ArrayList<>();
        int[] finalArray ;
        for (int i= 0; i< nums.length; i++) {
//            System.out.println(i);
            finalList.add(nums[i]);


        }
        Collections.sort(finalList);
        Integer numCounter = 0;
        for (int i= 0; i< finalList.size() ; i++) {
            Integer sortedNumber = finalList.get(i);
//            System.out.println(sortedNumber);
//            System.out.println(numCounter);
            if (!sortedNumber.equals(numCounter)) {
                System.out.print(numCounter);
            }
            numCounter ++ ;

        }

//            System.out.println(finalList);


    }



}
