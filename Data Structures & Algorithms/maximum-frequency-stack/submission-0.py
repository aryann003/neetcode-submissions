class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        f = self.freq[val]

        self.maxFreq = max(self.maxFreq, f)

        if f not in self.group:
            self.group[f] = []

        self.group[f].append(val)

    def pop(self) -> int:
        x = self.group[self.maxFreq].pop()

        self.freq[x] -= 1

        if not self.group[self.maxFreq]:
            self.maxFreq -= 1

        return x

