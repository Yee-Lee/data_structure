import sys, functools, threading

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []
    ##
    # request : (arrived_time, time_to_process)
    ##
    def process(self, request):
        # write your code here #######
        arrive_time = request[0]
        time_to_process = request[1]

        # for p in self.finish_time:
        #       if p <= arrive_time:
        #             flush_item += 1
        # self.finish_time = self.finish_time[flush_item:]
        
        ## optimize
        while len(self.finish_time) > 0 and self.finish_time[0] <= arrive_time:
              self.finish_time.pop(0)

        drop = False
        start_time = -1
        if len(self.finish_time) == 0:
              start_time = arrive_time
              finis_time = start_time + time_to_process
              self.finish_time.append(finis_time)
        elif len(self.finish_time) == self.size:
              drop = True
        else:
              start_time = self.finish_time[-1] 
              finis_time = start_time + time_to_process
              self.finish_time.append(finis_time)
        
        return (drop, start_time)

##
#  response :(True/False, start_time)
# #
def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, sys.stdin.readline().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, sys.stdin.readline().split())
        requests.append((arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response[1] if not response[0] else -1)

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
