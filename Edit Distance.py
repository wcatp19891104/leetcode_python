__author__ = 'wangzaicheng'


class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        dp = [[0] * (len(word2) + 1) for x in range(len(word1) + 1)]
        for i in range(len(word2) + 1):
            dp[0][i] = i
        for i in range(len(word1) + 1):
            dp[i][0] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1, dp[i - 1][j] + 1) if word1[i - 1] != word2[j - 1] else \
                    min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        return dp[len(word1)][len(word2)]


if __name__ == "__main__":
    s = Solution()
    print s.minDistance('a', 'ab')
