from typing import List
class Solution:
    def buyCrypto(self, prices: List[int]) -> int:
        minPrice = 1000;
        maxPrice = -1;
        for price in prices:
            minPrice = min(price, minPrice);
            maxPrice = max(price, maxPrice - minPrice);
            answer = maxPrice - minPrice;
            print(price, answer);
        return maxPrice

def main():
    testPrices = [10,1,5,6,7,1];
    print(Solution().buyCrypto(testPrices));

main();



