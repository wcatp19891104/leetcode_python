__author__ = 'wangzaicheng'
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        st = dict()
        i = 0
        for i in range(len(num)):
            if target - num[i] in st.keys():
                return st[target - num[i]], i + 1
            else:
                st[num[i]] = i + 1


