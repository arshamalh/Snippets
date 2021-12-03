import os
import multiprocessing
  
def start_worker(id):
    # pid => process id
    print(f"Worker {id} ID: {os.getpid()}")
  
if __name__ == "__main__":
    print(f"Main process ID: {os.getpid()}")
  
    # creating processes
    prss_1 = multiprocessing.Process(target=start_worker, args=(1, ))
    prss_2 = multiprocessing.Process(target=start_worker, args=(2, ))
  
    # starting processes
    prss_1.start()
    prss_2.start()
  
    # process IDs
    print(f"Process 1 ID: {prss_1.pid}")
    print(f"Process 2 ID: {prss_2.pid}")
  
    # wait until processes are finished
    prss_1.join()
    prss_2.join()
  
    print("Now, both processes are finished!")
  
    # check if processes are alive
    print("Process 1 is alive" if prss_1.is_alive() else "Process 1 is dead")
    print("Process 2 is alive" if prss_2.is_alive() else "Process 2 is dead")
    
    
# In multiprocessing, any newly created process will do following:
# - run independently
# - have their own memory space.

# *** References *** #
# https://www.geeksforgeeks.org/multiprocessing-python-set-1/
# https://www.geeksforgeeks.org/multiprocessing-python-set-2/

