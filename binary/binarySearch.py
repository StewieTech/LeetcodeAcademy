class Solution:
    def search(self, nums: List[int], target: int ) -> int:
        left, right = 0, len(nums);
        while left < right:
            mid = (left + right) / 2;
            return target if mid == target;

    def searchPython(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2;
            if nums[m] == target: return m;
            left, right = (mid + 1, r) if nums[mid] < target else (l , mid - 1);
        return - 1

def main():
    return 1; 

if __name__ == "__main__":
    main();

            