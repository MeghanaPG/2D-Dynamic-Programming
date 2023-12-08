class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Time Complexity:
        dp = {} #mapping (index,total) -> #no of ways 

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0 
            # if we have already seen this before 
            if (i,total) in dp:
                return dp[(i,total)]
            
            dp[(i,total)] = (backtrack(i+1, total+nums[i]) + 
                            backtrack(i+1, total-nums[i]))

            return dp[(i,total)]
        return backtrack(0,0)
