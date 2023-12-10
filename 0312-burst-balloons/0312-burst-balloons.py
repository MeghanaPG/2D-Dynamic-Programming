class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #Time Complexity: O(n^3) -> for each of the loops we will have to run atleast once, which gives us the O(n^3) time complexity 
        # we are gonna be updating the array 
        # adding 1 at the beginning and adding 1 at the end 
        nums = [1] + nums + [1]
        # cache
        dp = {}

        def dfs(l,r):
            # base case 
            # if left past the right pointer, that means we ran out of balloons and hence we return 0 
            if l > r: 
                return 0 

            if (l,r) in dp:
                return dp[(l,r)]
            
            dp[(l,r)] = 0 
            for i in range(l, r+1):
                # if nums[i] was popped last 
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                dp[(l,r)] = max(dp[(l,r)], coins)
            return dp[(l,r)]
        # calling the function 
        return dfs(1,len(nums)-2)
