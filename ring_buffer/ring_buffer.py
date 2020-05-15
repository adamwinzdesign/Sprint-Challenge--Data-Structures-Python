class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.oldest = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            self.data.remove(self.data[self.oldest])
            self.data.insert(self.oldest, item)
            if self.oldest+1 < self.capacity:
                self.oldest += 1
            else:
                self.oldest = 0

    def get(self):
        for i in self.data:
            if self.data == None:
                self.data.remove(self.data[i])
        return(self.data)
