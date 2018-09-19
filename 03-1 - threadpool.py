from time import sleep, strftime
from concurrent import futures

# a simple display function to print time and any args passed to it
def display(*args):   
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):   
    """ A loiter function thta does nothing but print messages 
     by indenting tab according to the args passed to it 
    """
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t'*n, n, n))
    # Calling sleep releases the GIL
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n * 10


def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3)   
    results = executor.map(loiter, range(5))   
    display('results:', results)  #  .
    display('Waiting for individual results:')
    for i, result in enumerate(results):   
        display('result {}: {}'.format(i, result))


if __name__ == '__main__':        
    main()
