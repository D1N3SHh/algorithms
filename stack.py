# basic stack implementation
# author: D1N3SHh
# https://github.com/D1N3SHh/algorithms


class StackOverflowError(BaseException):
    pass

class StackEmptyError(BaseException):
    pass


class Stack():
    def __init__(self, max_size = 10):
        self.max_size = max_size
        self.s = []
        
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


if __name__ == "__main__":
    stack = Stack(5)

    # --short test--
    # should be:
    #   1234
    #   [9998, 9999] 
    
    stack.push(9998)
    stack.push(1234)
    stack.push(5656)
    stack.pop()
    print(stack.peek())
    stack.push(9999)
    print(stack.s)