class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bottom Up
        # Time Complexity: O(n * m)
        dp = [[ 0 for j in range(len(text2) +1)] for i in range(len(text1) + 1)]

        # traversing the 2D grid in reverse order
        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                # we take from diagonal if there is a match
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    # max of (right, below)
                    # we don't add 1 here as the characters don't match 
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        # res will be at top left
        return dp[0][0]