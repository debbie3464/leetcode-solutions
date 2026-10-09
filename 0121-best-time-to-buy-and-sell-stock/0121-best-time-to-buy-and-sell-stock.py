class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')  
        best_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > best_profit:
                best_profit = price - min_price

        return best_profit
        
        