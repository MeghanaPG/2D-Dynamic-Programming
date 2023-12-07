class Solution {
    public int uniquePaths(int m, int n) {
      // Time Complexity: O(m*n)
        int[] dp = new int[n];
        for (int i = 0; i < m; i++) {
          for (int j = 0; j < n; j++) {
            if (i == 0) {
              dp[j] = 1;
            }
            else if (j == 0) {
              dp[j] = 1;
            }
            else {
              dp[j] = dp[j] + dp[j-1];
            }
          }
        }

        return dp[n-1];
    }
}