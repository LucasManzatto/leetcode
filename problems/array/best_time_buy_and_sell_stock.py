# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        min_value = prices.pop(0)
        max_profit = 0

        for current_value in prices:
            min_value = min(min_value, current_value)
            current_profit = current_value - min_value
            max_profit = max(max_profit, current_profit)

        return max_profit


    def maxProfit2(self, prices: List[int]) -> int:
        left = 0  # Pointer for buying
        right = 1  # Pointer for selling

        max_profit = 0

        while right < len(prices):
            # Check if the price at the buying pointer is greater than the price at the selling pointer
            # If so, update the buying pointer to the selling pointer
            if prices[left] > prices[right]:
                left = right
            else:
                # Calculate the current profit by subtracting the buying price from the selling price
                current_profit = prices[right] - prices[left]
                # Update the maximum profit if the current profit is greater
                max_profit = max(max_profit, current_profit)

            right += 1
        return max_profit


prices = [7, 1, 5, 3, 6, 4]
result = Solution().maxProfit2(prices=prices)
