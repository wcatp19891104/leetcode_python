__author__ = 'wangzaicheng'


class Solution:

    def reverse(self,s):
        s = s[::-1]
        return s

    def reverseWords(self, s):
        s = s[::-1]
        part = str()
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                t = self.reverse(part)
                s = s[:start] + t + s[start + len(part):]
                part = str()
                start = i + 1
            else:
                part += s[i]
        return s


if __name__ == "__main__":
    s = Solution()
    print s.reverseWords("I have a dream")
