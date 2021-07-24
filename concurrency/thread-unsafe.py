# import dis

# count = 0

# def increment():
#     global count
#     count += 1

# # prints the bytecode
# dis.dis(increment)

from threading import Thread
import sys

class Counter:

    def __init__(self):
        self.count = 0

    def increment(self):
        for _ in range(100000):
            self.count += 1


if __name__ == "__main__":
    
    # Sets the thread switch interval
    sys.setswitchinterval(0.005)

    numThreads = 5
    threads = [0] * numThreads
    counter = Counter()

    for i in range(0, numThreads):
        threads[i] = Thread(target=counter.increment)

    for i in range(0, numThreads):
        threads[i].start()

    for i in range(0, numThreads):
        threads[i].join()

    if counter.count != 500000:
        print(f'count: {counter.count}')
    else:
        print(" count = 500,000 - Try re-running the program.")

