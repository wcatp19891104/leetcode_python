__author__ = 'wangzaicheng'
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        vote = num[0]
        count = 1
        num = num[1:]
        for item in num:
            if item == vote:
                count += 1
            else:
                count -= 1
                if count == 0:
                    vote = item
                    count = 1
        return vote