__author__ = 'wangzaicheng'
class Solution:
    # @return a boolean
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False
        st = list()
        for char in s:
            if char in {'(', '{', '['}:
                st.append(char)
            else:
                if len(st) == 0:
                    return False
                mark = st.pop()
                if (mark, char) not in {('(', ')'), ('{','}'), ('[', ']')}:
                    return False
        if len(st) != 0:
            return False
        return True

