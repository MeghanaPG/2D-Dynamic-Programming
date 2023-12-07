class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Time and Space Complexity: O(m*n)

        cache = {}

        def dfs(i,a):
          if a == amount:
            return 1 
          
          if a > amount: 
            return 0 

          # if we go out of bounce 
          if i == len(coins):
            return 0 

          # if we already computed it 
          if (i,a) in cache:
            return cache[(i,a)]
          
          # two decisions: coin at index i and case if we skip the index i 
          cache[(i,a)] = dfs(i, a+coins[i]) + dfs(i+1, a)
          return cache[(i,a)]

        return dfs(0,0)
