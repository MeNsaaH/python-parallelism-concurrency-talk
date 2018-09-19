import threading
import itertools
import time
import sys

# Using Multi Threading to perform parallel Logging 

class Signal:   
    go = True

    
def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):   
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))   
        time.sleep(.1)
        if not signal.go:   
            break
    write(' ' * len(status) + '\x08' * len(status))
    
def slow_function():   
    # pretend waiting a long time for I/O
    time.sleep(3)   
    return 42


def supervisor():   
    signal = Signal()
    spinner = threading.Thread(target=spin,
                               args=('thinking!', signal))
    print('spinner object:', spinner)   
    spinner.start()   
    result = slow_function()  
    # major issue with threading is terminating
    # set signal.go in main thread so it is read from other threads
    # threads have access to the same memory 
    signal.go = False   
    spinner.join()   
    return result


def main():
    result = supervisor()   
    print('Answer:', result)

    
if __name__ == '__main__':
    main()
