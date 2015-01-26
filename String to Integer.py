__author__ = 'wangzaicheng'

class Solution:
    # @return an integer
    def atoi(self, str):
        i = 0
        str = str.strip()
        if len(str) == 0:
            return 0
        flag = -1 if str[0] == '-' else 1
        ret = 0
        for i in range(len(str)):
            if not str[i].isdigit():
                if str[i] in {'-', '+'} and i == 0:
                    continue
                return ret * flag
            ret = ret * 10 + int(str[i])
        return ret * flag


if __name__ == "__main__":
    s = Solution()
    s.atoi('  -0012a42')