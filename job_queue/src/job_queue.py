import sys, functools, threading

def assign_jobs_naive(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append((next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


##
##  Build a priority queue of n threads. Each thread has a priority value of free time.
##  When a thread is poped out from queue, assign it a job and a new free time value and put it back to the queue.
##
def assign_jobs(n_workers, jobs):
  import heapq

  #Each node is a thread with (free_time, index)
  nodes = [[0, x] for x in range(n_workers)] 
  heapq.heapify(nodes)

  ret = []
  for job in jobs:
    n = heapq.heappop(nodes)
    ret.append((n[1], n[0]))
    n[0] = n[0] + job
    heapq.heappush(nodes, n)

  return ret

def main():
    data = sys.stdin.read().split()
    n_workers, n_jobs = map(int, data[0:2])
    jobs = list(map(int, data[2:]))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print "%d %d"%(job[0], job[1])

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
