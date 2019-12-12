import sys, functools, threading


##
# Implemented using 2 stacks.
##
class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__maxStack = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.__maxStack) == 0:
            self.__maxStack.append(a)
        else:
            if self.__maxStack[-1] <= a:
                self.__maxStack.append(a)
            else: self.__maxStack.append(self.__maxStack[-1]) 

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.__maxStack.pop()

    def Max(self):
        return self.__maxStack[-1]
        
        
def main():
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)

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
