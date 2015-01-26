__author__ = 'wangzaicheng'


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join({s[i].strip() for i in range(len(s) - 1, -1, -1)})

if __name__ == "__main__":
    s = Solution()
    s.reverseWords('s')