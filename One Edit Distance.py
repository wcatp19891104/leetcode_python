__author__ = 'wangzaicheng'


def OneEditDistance(S, T):
    S, T = (S, T) if len(S) <= len(T) else (T, S)
    if len(T) - len(S) > 1:
        return False
    change = 0
    if len(T) == len(S):
        for i in range(len(S)):
            if S[i] != T[i]:
                change += 1
            if change > 1:
                return False
        return True
    else:
        for i in range(len(S)):
            if S[i] != T[i]:
                if S[i:] == T[i + 1:]:
                    return True
                return False
        return True


if __name__ == "__main__":
    print OneEditDistance('abcd', 'abxd')

