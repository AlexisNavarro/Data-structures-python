#Queue's are normally said to accept data on a first in first out(FIFO) basis

from collections import deque
from queue import Queue
def reg_queue():
    print("accessed regular queue method")

    user_in= int(input("1. create a queue from deque import \n2. create a queue from queue import "))

    if user_in == 1:
        q = deque()

        #add to queue
        q.append("Alexis")
        q.append("Jose")
        q.append("John")

        
        #pop from queue using pop
        print("popping value from queue", q.pop())

        print("queue after popping", q)

        #pop from queue using popleft
        print(q.popleft())

    elif user_in == 2:

        q = Queue(maxsize = 5)

        print(q.qsize())

        q.put("Alexis")
        q.put("Jose")
        q.put("John")
        q.put("Steven")
        q.put("Bill")

        print("Full", q.full())

        #print(q.get())

        for i in range(q.qsize()):
            print(q.get(i))


        print("Full", q.full())



def prio_queue():
    print("accessed priority queue method")


def main():
    user_in= int(input("1. create a regular queue \n2. create a priority queue "))

    match user_in:
        case 1:
            reg_queue()
        case 2:
            prio_queue()

if __name__ == '__main__':
    main()