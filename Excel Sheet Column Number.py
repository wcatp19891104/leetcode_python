__author__ = 'wangzaicheng'
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        if s == str():
            return 0
        ret = 0
        i = 0
        factor = 1
        for i in range(len(s) - 1, -1, -1):
            ret += (ord(s[i]) - ord('A') + 1) * factor
            factor *= 26
        return ret