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
from threading import Thread
import time

def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)

threads = []
num_threads = 10
# print(num_processes)

# create processes
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# start processes

for t in threads:
    t.start() 
    
# join
for t in threads:
    t.join()


print('end main')