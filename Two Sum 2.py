__author__ = 'wangzaicheng'


class Solution:
    def twoSum2(self, num, target):
        start = 0
        end = len(num) - 1
        while start < end:
            sum = num[start] + num[end]
            if sum == target:
                return start, end
            elif sum > target:
                end -= 1
            else:
                start += 1

