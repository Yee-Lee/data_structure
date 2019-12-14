import sys, functools, threading

##
# Implemented a queue by 2 stacks with an amortized constant runtime
# Add the feature of max into the stacks.
##
class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__maxStack =[]
    def push(self, a):
        self.__stack.append(a)
        if len(self.__maxStack) == 0 : self.__maxStack.append(a)
        else:
            if a >= self.__maxStack[-1]: self.__maxStack.append(a)
            else: self.__maxStack.append(self.__maxStack[-1])

    def pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.__maxStack.pop()

    def top(self):
        return self.__stack[-1]
    
    def empty(self):
        return len(self.__stack) == 0

    def max(self):
        return self.__maxStack[-1] if len(self.__maxStack) else -sys.maxint-1

class QueueWithMax():
    def __init__(self):
        self.s1 = StackWithMax()
        self.s2 = StackWithMax()
        self.__len = 0

    def __transport(self):
        while(not self.s1.empty()):
            self.s2.push(self.s1.top())
            self.s1.pop()

    def __len__(self):
        return self.__len

    def enQueue(self, a):
        self.s1.push(a)
        self.__len += 1

    def deQueue(self):
        assert(not self.s2.empty() or not self.s1.empty())
        if( self.s2.empty()):
            self.__transport()
        self.s2.pop()
        self.__len -= 1

    def max(self):
        return max(self.s1.max(), self.s2.max())


def max_sliding_window(seq, m):
    maximums = []
    q = QueueWithMax()
    for i in range(len(seq)):
        q.enQueue(seq[i])
        if len(q) > m:
            q.deQueue()
        if len(q) == m:
            maximums.append(q.max())
    return maximums

## NAIVE IMPLEMNTATION
def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums
        
def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    input_sequence = [int(i) for i in data[1:n+1]]
    assert len(input_sequence) == n
    window_size = int(data[-1])

    print(" ".join(str(x) for x in max_sliding_window(input_sequence, window_size)))

MAINFUNC = main
###########################################################################################
import traceback

if __name__ == '__main__':
  try:
    threading.Thread(target=main).start()
  except Exception as e:
    details = traceback.format_exc()
    print "\nRuntime error: %s\n\n %s"%(e, details)
  else:
    pass
