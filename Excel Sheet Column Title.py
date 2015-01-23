__author__ = 'wangzaicheng'
class Solution:
    # @return a string
    def convertToTitle(self, num):
        if num == 0:
            return str()
        ret = str()
        while (num - 1) / 26 != 0:
            curr = (num - 1) % 26
            ret = chr(curr + ord('A')) + ret
            num = (num - 1) / 26
        ret = chr(num - 1 + ord('A')) + ret
        return ret
