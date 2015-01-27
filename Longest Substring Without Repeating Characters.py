__author__ = 'wangzaicheng'


class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        """
        two pointer, when find duplicate, slow move to the first duplicate char
        :param s:
        :return:
        """
        if len(s) == 0:
            return 0
        rem = set()
        max = 1
        slow = 0
        fast = 0
        while slow < len(s) and fast < len(s):
            if s[fast] not in rem:
                rem.add(s[fast])
                max = len(rem) if len(rem) > max else max
                fast += 1
            elif s[fast] in rem and fast != slow:
                max = len(rem) if len(rem) > max else max
                while s[slow] != s[fast]:
                    rem.remove(s[slow])
                    slow += 1
                rem.remove(s[slow])
                slow += 1

        return max


if __name__ == "__main__":
    s = Solution()
    s.lengthOfLongestSubstring('ohomm')