from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) ->  List[int]:
        l,r = 0, len(numbers) - 1;

        while l < r:
            currSum = numbers[l] + numbers[r];
            print(currSum, target);
            if currSum < target:
                 l += 1;
            elif currSum > target:
                r -= 1;
            else :
                return [l +1, r+1]

def main() :
    testArray = [1,2,3,4];
    print(Solution().twoSum(testArray,3));

if __name__ == "__main__":
    main();

