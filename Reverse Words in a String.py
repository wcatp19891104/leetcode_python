__author__ = 'wangzaicheng'


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.split(' ')
        return ' '.join([s[i] for i in range(len(s) - 1, -1, -1) if s[i] != ''])

if __name__ == "__main__":
    s = Solution()
    s.reverseWords('s')