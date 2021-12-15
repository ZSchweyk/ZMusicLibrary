class FlexibleList:
    def __init__(self, lst: list):
        self.lst = lst

    def __iter__(self):
        return iter(self.lst)

    def __getitem__(self, i):
        i %= len(self.lst)
        return self.lst[i]

    def __delitem__(self, i):
        i %= len(self.lst)
        del self.lst[i]

    def __setitem__(self, i, val):
        self.lst[i] = val
