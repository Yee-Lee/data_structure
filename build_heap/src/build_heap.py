import sys, functools, threading


def build_heap_by_selection_sort(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

_swaps = []

def heapify(data, n, i):
  
  lc = 2*i+1
  rc = 2*i+2
  smallest = i
  if(lc < n and data[lc]<data[smallest]):
    smallest = lc
  if(rc < n and data[rc]<data[smallest]):
    smallest = rc
  if(smallest != i):
    tmp = data[i]
    data[i] = data[smallest]
    data[smallest] = tmp
    _swaps.append((i, smallest))
    heapify(data, n, smallest)

  

def build_heap(data):

  #last non-leaf node
  k = ((len(data)-1)-1)/2
  for i in range(k, -1, -1):
    heapify(data, len(data), i) 

  return _swaps


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    d = list(map(int, data[1:]))
    assert len(d) == n

    swaps = build_heap(d)

    print(len(swaps))
    for i, j in swaps:
        print "%d %d"%(i, j)


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
