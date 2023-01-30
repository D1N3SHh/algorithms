# queue algorithm
# time complexity: O(1)
# auxiliary space: O(n)


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

    def __repr__(self):
        return str(self.q)

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


def example_usage():
    queue = Queue(5)                         # [NULL, NULL, NULL, NULL, NULL]
    queue.enqueue(1111)                      # [1111, NULL, NULL, NULL, NULL]
    queue.enqueue(2222)                      # [1111, 2222, NULL, NULL, NULL]
    queue.enqueue(3333)                      # [1111, 2222, 3333, NULL, NULL]
    print('Queue:', queue)
    print('Dequeue:', queue.dequeue())       # [NULL, 2222, 3333, NULL, NULL]
    queue.enqueue(4444)                      # [NULL, 2222, 3333, 4444, NULL]
    print('Queue:', queue)


if __name__ == "__main__":
    example_usage()