class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time Complexity: O(n)
        # State: Buying or Selling? 
        # If Buy -> i+1
        # If Sell -> i+2 because of the cooldown period 

        dp = {} # key = (i, buying) val = max_profit 

        # buying -> flag 
        def dfs(i, buying):
          if i >= len(prices):
            return 0 
          
          if (i, buying) in dp:
            return dp[(i, buying)]

          if buying:
            buy = dfs(i+1, not buying) - prices[i]
            cooldown = dfs(i+1, buying)
            # to know the max profit so far 
            dp[(i, buying)] = max(buy, cooldown)
          else:
            # add prices[i] because if we sold, we made some money 
            sell = dfs(i+2, not buying) + prices[i]
            cooldown = dfs(i+1, buying)
            dp[(i, buying)] = max(sell, cooldown)
          return dp[(i, buying)]
        return dfs(0, True)


