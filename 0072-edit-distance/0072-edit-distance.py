class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Time Complexity: O(m.n)
        cache = [[float("inf")] * (len(word2)+1) for i in range(len(word1)+ 1)]

        # filling in the last column and last row of cache 
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j 
        for i in range(len(word1)+1):
            cache[i][len(word2)] = len(word1) - i 

        # now we can fill up the rest, bottom up approach 
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    # we have to check all three directions and take the min of those 
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])
        return cache[0][0]

