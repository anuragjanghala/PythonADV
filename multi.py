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
import time


def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1
        

if __name__ == '__main__':
    
    lock = Lock()
    #shared_number = Value('i', 0)
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('array at beginning is', shared_array[:])
    
    p1= Process(target=add_100, args=(shared_array,lock))
    p2 = Process(target=add_100, args=(shared_array,lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print('array at the end is ', shared_array[:])
