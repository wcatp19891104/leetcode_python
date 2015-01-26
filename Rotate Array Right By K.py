__author__ = 'wangzaicheng'


class Solution:
    def rotateArrayRightByK(self, num, K):
        for i in range(K):
            num.insert(0, num.pop())
        return num


if __name__ == "__main__":
    s = Solution()
    print s.rotateArrayRightByK([0, 1, 2, 3, 4, 5, 6], 3)