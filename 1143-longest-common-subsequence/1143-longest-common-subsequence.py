class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Time Complexity: O(m*n) (length of strings mutliplied by each other)
        # 2D grid with 0's in it 
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        # we will traverse from bottom right to top left 
        for i in range(len(text1)-1, -1, -1):
          for j in range(len(text2)-1, -1, -1):
            if text1[i] == text2[j]:
              # 1 + diagonal
              dp[i][j] = 1 + dp[i+1][j+1]
            else:
              # max(right value, bottom value)
              dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]
