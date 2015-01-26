__author__ = 'wangzaicheng'
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if len(needle) is 0:
            return 0
        if len(haystack) is 0:
            return -1
        if len(needle) > len(haystack):
            return -1
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            start = i
            if len(haystack) - i < len(needle):
                return -1
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == len(needle):
                return start
            else:
                j = 0
                i = start + 1
        return -1
