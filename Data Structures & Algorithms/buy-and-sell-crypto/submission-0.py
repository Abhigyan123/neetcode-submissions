class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy =prices[0]
        max_profit=0
        # max_buy =[0]
        for i in range(1,len(prices)):
            if min_buy>prices[i]:
                min_buy = prices[i]
            elif prices[i]-min_buy>max_profit:
                max_profit = prices[i]-min_buy

        return (max_profit)
           

        