class MyHash:
    def __init__(self, b) -> None:
        self.BUCKET = b
        self.hTable = [[] for x in range(b)]

    def insert(self, x):
        key = x % self.BUCKET
        self.hTable[key].append(x)

    def remove(self, x):
        key = x % self.BUCKET
        if x in self.hTable[key]:
            self.hTable[key].remove(x)

    def search(self, x):
        key = x % self.BUCKET
        return x in self.hTable[key]


if __name__ == "__main__":
    h = MyHash(7)

    h.insert(70)
    h.insert(71)
    h.insert(9)
    h.insert(56)
    h.insert(72)

    print(h.search(56))

    h.remove(56)

    print(h.search(56))
