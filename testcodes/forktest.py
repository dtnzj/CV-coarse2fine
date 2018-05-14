from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def processInit():
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        print('i = ', i)
        p.apply_async(long_time_task, args=(i,))
        
        # p.apply_async(long_time_task, args=(2,))
        # p.apply_async(long_time_task, args=(3,))
        # p.apply_async(long_time_task, args=(4,))
        # p.apply_async(long_time_task, args=(5,))
        
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
    


if __name__=='__main__':
    
    processInit()

    print('Program End wait for exit')

    input('wait key')
    