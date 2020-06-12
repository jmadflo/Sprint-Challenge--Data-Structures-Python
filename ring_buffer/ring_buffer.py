class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.content = []
        self.oldest = -1

    def append(self, item):
        if len(self.content) < self.capacity:
            self.content.append(item)
        else:
            if self.oldest >= self.capacity - 1:
                self.oldest = 0
            else:
                self.oldest += 1
            self.content[self.oldest] = item
    def get(self):
        return self.content