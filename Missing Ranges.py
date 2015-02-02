__author__ = 'wangzaicheng'


def get_range(pre, curr):
    if curr - pre == 2:
        return str(curr - 1)
    return '->'.join([str(pre + 1), str(curr - 1)])


def Missing_ranges(Array, start, end):
    ret = list()
    pre = start - 1
    Array.append(end + 1)
    for item in Array:
        curr = item
        if curr - pre >= 2:
            ret.append(get_range(pre, curr))
        pre = curr
    return ret


if __name__ == "__main__":
    print Missing_ranges([0, 1, 3, 50, 99], 0, 99)
    print Missing_ranges([], 0, 99)
    print(Missing_ranges([1, 99], 0, 99))
    print(Missing_ranges([0, 99], 0, 99))
