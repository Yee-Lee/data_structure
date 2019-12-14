import sys, functools, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class Tree:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  ret = []
  def travel(i):
    if i == -1: return
    travel(tree.left[i])
    ret.append(tree.key[i])
    travel(tree.right[i])
  travel(0)

  for i in range(len(ret)-1):
    if ret[i] > ret[i+1]: return False
  return True


def main():
  tree = Tree()
  tree.read()
  if IsBinarySearchTree(tree):
    print(1)
  else:
    print(0)

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
