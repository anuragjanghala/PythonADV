# with open('notes.txt', 'w') as file:
#     file.write('some todoo...')
    
# file = open('notes.txt', 'w')
# try:
#     file.write('some todoo...')
# finally:
#     file.close()
    
    
##########################################

# from threading import Lock

# lock = Lock()

# lock.acquire()
# #...........
# lock.release()

# with lock:
#     #....

##########################################

class ManagedFile:
    def __init__(self, fileName) -> None:
        print('init')
        self.fileName = fileName

    def __enter__(self):
        print('Enter')
        self.file = open(self.fileName,'w')
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        #print('exc:', exc_type, exc_value)
        print('exit')
        return True


with ManagedFile('notes.txt') as file:
    print('do some stuff...')
    file.write('some todo...')
    file.somemethod() # using this to create exception
print('continuing')