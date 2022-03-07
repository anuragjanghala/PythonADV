# from multiprocessing import Process
# from multiprocessing.dummy import freeze_support
# import os
# import time


# def square_numbers():
#     for i in range(100):
#         i*i
#         time.sleep(0.1)

# processes = []
# num_processes = os.cpu_count()
# # print(num_processes)

# # create processes
# for i in range(num_processes):
#     p = Process(target=square_numbers)
#     processes.append(p)

# # start processes
# if __name__ == '__main__':
#     freeze_support()
#     for p in processes:
#         p.start() 
    
#     # join
#     for p in processes:
#         p.join()
    

    
# print('end main')


##################################################################
# from threading import Thread
# import time

# def square_numbers():
#     for i in range(100):
#         i*i
#         time.sleep(0.1)

# if __name__ == '__main__':
#     threads = []
#     num_threads = 10
    
#     for i in range(num_threads):
#         t = Thread(target=square_numbers)
#         threads.append(t)

#     # start threads

#     for t in threads:
#         t.start() 
        
#     # join threads: wait for them to complete
#     for t in threads:
#         t.join()


# print('end main')

##################################################################

from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
import time


def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1
        

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)
        
def make_negative(numbers,queue):
    for i in numbers:
        queue.put(-1*i)

if __name__ == '__main__':
    
    numbers = range(1,6)
    q = Queue()
    
    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))
    
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    while not q.empty():
        print(q.get())
