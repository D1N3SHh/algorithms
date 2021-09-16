# basic queue implementation
# author: D1N3SHh
# https://github.com/D1N3SHh/algorithms


class QueueOverflowError(BaseException):
    pass

class QueueEmptyError(BaseException):
    pass


class Queue():
    def __init__(self, max_size = 10):
        self.max_size = max_size
        self.q = [None] * max_size
        self.tail = 0
        self.head = 0

    def enqueue(self, x):
        if self.tail == self.max_size:
            raise QueueOverflowError
        else:
            self.q[self.tail] = x
            if self.tail == self.max_size - 1:
                self.tail = 0
            else:
                self.tail += 1

    def dequeue(self):
        if self.head == self.tail + 1:
            raise QueueEmptyError
        else:
            x = self.q[self.head]
            self.q[self.head] = None
            if self.head == self.max_size - 1:
                self.head = 0
            else:
                self.head += 1
            return x


if __name__ == "__main__":
    queue = Queue(5)
    
    # --short test--
    # should be:
    #   1234
    #   [None, 9999, 8888, 7777, None] 
    
    queue.enqueue(1234)
    queue.enqueue(9999)
    queue.enqueue(8888)
    print(queue.dequeue())
    queue.enqueue(7777)
    print(queue.q)