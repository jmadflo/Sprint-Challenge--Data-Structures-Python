class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.content = []
        self.replace = -1

    def append(self, item):
        if len(self.content) < self.capacity:
            self.content.append(item)
        else:
            if self.replace >= self.capacity - 1:
                self.replace = 0
            else:
                self.replace += 1
            self.content[self.replace] = item
    def get(self):
        return self.content