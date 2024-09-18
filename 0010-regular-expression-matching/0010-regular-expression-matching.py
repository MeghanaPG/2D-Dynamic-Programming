class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Top down memoization 
        # Time Complexity: 
        cache = {}

        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            # star has the precedence
            if (j+1) < len(p) and p[j+1] == "*":
                # 2 choices don't use the star or use the star
                cache[(i,j)] = (dfs(i,j+2) or (match and dfs(i+1, j)))
                return cache[(i,j)]

            if match:
                cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)]
            cache[(i,j)] = False 
            return False 
        return dfs(0,0)
