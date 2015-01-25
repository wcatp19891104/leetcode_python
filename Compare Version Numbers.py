__author__ = 'wangzaicheng'
class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        list1 = version1.split('.')
        list2 = version2.split('.')
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            num1 = int(list1[i])
            num2 = int(list2[j])
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            else:
                i += 1
                j += 1
        if i < len(list1) and int(list1[i]) != 0:
            return 1
        elif j < len(list2) and int(list2[j]) != 0:
            return -1
        else:
            return 0
