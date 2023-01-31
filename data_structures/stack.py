# basic stack implementation
# time complexity: o(1)
# auxiliary space: O(1)


class StackOverflowError(BaseException):
    pass

class StackEmptyError(BaseException):
    pass


class Stack():
    def __init__(self, max_size = 10):
        self.max_size = max_size
        self.s = []

    def __repr__(self):
        return str(self.s)
        
    def push(self, x):
        if len(self.s) < self.max_size:
            self.s.append(x)
        else: raise StackOverflowError

    def pop(self):
        if len(self.s) > 0: 
            self.s.pop(-1)
        else: raise StackEmptyError

    def peek(self):
        x = self.s[-1]
        self.pop()
        return x


def example_usage():
    stack = Stack(5)                    # []
    stack.push(1111)                    # [1111]
    stack.push(2222)                    # [1111, 2222]
    stack.push(3333)                    # [1111, 2222, 3333]
    print('Stack:', stack)
    print('Peek:', stack.peek())        # [1111, 2222]
    stack.push(4444)                    # [1111, 2222, 4444]
    print('Stack:', stack)


if __name__ == "__main__":
    example_usage()