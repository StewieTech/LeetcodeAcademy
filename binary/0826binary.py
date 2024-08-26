from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) -1;
        while (l <= r):
            mid = l + ((r - l) //  2);
            if nums[mid] < target:
                l = mid + 1;
            elif (nums[mid] > target):
                r = mid - 1;
            else:
                print(mid)
                return mid;
        return - 1;

def main():
    testNumbers = [-1,0,2,4,6,8];
    print(Solution().search(testNumbers,4));
main();




