class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Time complexity: O(m.n)
        cache = {}

        def dfs(i,j):
            # string t is empty 
            if j == len(t):
                return 1 
            # string s is empty 
            if i == len(s):
                return 0 
            # 3rd base case 
            if (i,j) in cache:
                return cache[(i,j)]
            
            if s[i] == t[j]:
                # dfs(i + 1, j) part is because we will be able to find the t even with different indexes of the s as we can see in the first example 
                cache[(i,j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i,j)] = dfs(i + 1, j)
            return cache[(i,j)]
        return dfs(0,0)
