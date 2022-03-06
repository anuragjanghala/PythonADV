from threading import Thread, Lock
import time

database_value = 0

def increase(lock):
    global database_value
    
    # lock will lock the state so it wont switch to thread2 and if we remove lock it will switch and answer will result to 1 instead of 2.
    with lock:
        #lock.acquire()
        local_cpy = database_value
        # processing
        local_cpy += 1
        time.sleep(0.1)
        database_value = local_cpy
        #lock.release()


if __name__ == '__main__':
    
    lock = Lock()
    print('start value', database_value)
    
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print('end value', database_value)

    print('end main')