__author__ = 'wangzaicheng'


class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""

        dp = [[0 for x in range(len(s))] for x in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        max = 0
        ret = str()
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i - j < 2:
                    dp[j][i] = s[i] == s[j]
                else:
                    dp[j][i] = dp[j + 1][i - 1] and s[i] == s[j]
                if dp[j][i] and j - i + 1 > max:
                    ret = s[j: i + 1]
                    max = i - j + 1
        return ret


if __name__ == "__main__":
    s = Solution()
    print s.longestPalindrome('a')

