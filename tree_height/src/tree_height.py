import sys, functools, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
      def __init__(self, index):
            self.index = index
            self.children = []
      def addChild(self, child):
            self.children.append(child)

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                tree = [Node(i) for i in range(self.n)]
                
                for i in range(self.n):
                      p = self.parent[i]
                      if p == -1:
                            self.root = tree[i]
                      else:
                            tree[p].addChild(tree[i])
                
                #BFS
                import Queue
                q = Queue.Queue()
                height = 0
                q.put(self.root)
                while not q.empty():
                      size = q.qsize()
                      height += 1
                      for j in range(size):
                        nd = q.get()
                        [q.put(ch) for ch in nd.children]
                
                return height 

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

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
