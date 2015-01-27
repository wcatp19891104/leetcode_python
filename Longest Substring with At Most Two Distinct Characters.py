__author__ = 'wangzaicheng'


class Solution:

    def LS2(self, s):
        """
        Given a string S, find the length of the longest substring T that contains at most two distinct characters.
        For example,
        Given S = eceba,
        T is "ece" which its length is 3.
        :param s:
        :return:
        """
        max = 1
        i = 0 # mark the start
        j = -1 # mark the first different one
        k = 0 # mark the end
        for k in range(len(s)):
            if k == 0 or s[k] == s[k - 1]:
                continue
            elif j >= 0 and s[j] != s[k]:
                max = k - i if k - i > max else max
                i = j + 1
            j = k - 1
        return max


if __name__ == "__main__":
    s = Solution()
    print s.LS2('eceba')

