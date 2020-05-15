class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.oldest = 0

    def append(self, item):
        # if current length of self.data is less than the provided capacity, simply add that item to data
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            # if current length of self.data is equal to the provided capacity, remove the oldest item, then insert the new item where the oldest item had been
            self.data.remove(self.data[self.oldest])
            self.data.insert(self.oldest, item)
            # determine if we need to increment oldest or reset it to 0
            if self.oldest == self.capacity -1:
                self.oldest = 0
            else:
                self.oldest += 1

    def get(self):
        for i in self.data:
            if self.data == None:
                self.data.remove(self.data[i])
        return(self.data)
