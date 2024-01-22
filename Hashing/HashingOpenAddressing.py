class MyHash:
    def __init__(self, c) -> None:
        self.cap = c
        self.table = [-1] * c
        self.size = 0

    def hash(self, x):
        return x % self.cap

    def search(self, x):
        hashValue = self.hash(x)
        hTable = self.table
        i = h

        while (hTable[i] != -1):
            # Key found
            if (hTable[i] == x):
                return True
            # Incresing the index in an circular manner
            i = (i + 1) % self.cap
            # Whole table is full and key is not there
            if (i == hashValue):
                return False
        # Stop at empty spot
        return False

    def insert(self, x):
        # When table is already full
        if self.size == self.cap:
            return False

        # When key is already present
        if self.search(x) == True:
            return False

        i = self.hash(x)
        hTable = self.table

        # -1 = empty and -2 = deleted
        while hTable[i] not in (-1, -2):
            i = (i + 1) % self.cap

        # Insert the key, increase size and return True
        hTable[i] = x
        self.size = self.size + 1
        return True

    def remove(self, x):
        h = self.hash(x)
        hTable = self.table
        i = h

        while hTable[i] != -1:
            if hTable[i] == x:
                # Mark deleted by -2
                hTable[i] = -2
                return True
            i = (i + 1) % self.cap
            if i == h:
                return False
        return False


if __name__ == "__main__":
    h = MyHash(7)

    h.insert(49)
    h.insert(56)
    h.insert(72)

    print(h.search(56))
    h.remove(56)

    print(h.remove(56))
    print(h.search(56))
