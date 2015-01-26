__author__ = 'wangzaicheng'


class TwoSum:
    def __init__(self):
        self.st = set()

    def add(self, num):
        self.st.add(num)

    def find(self, target):
        for item in self.st:
            if target - item in self.st:
                return True
        return False


if __name__ == "__main__":
    t = TwoSum()
    t.add(1)
    t.add(3)
    t.add(5)
    print t.find(4), t.find(7)
