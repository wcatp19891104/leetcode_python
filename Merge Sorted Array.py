__author__ = 'wangzaicheng'
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = m - 1
        j = n - 1
        curr = m + n - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[curr] = A[i]
                i -= 1
                curr -= 1
            else:
                A[curr] = B[j]
                j -= 1
                curr -= 1
        if j >= 0:
            A[: curr + 1] = B[: j + 1]


