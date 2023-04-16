#Queue's are normally said to accept data on a first in first out(FIFO) basis

from collections import deque
from queue import Queue
import queue

def reg_queue():
    print("accessed regular queue method")

    user_in= int(input("1. create a queue from deque import \n2. create a queue from Queue import "))

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
    user_in= int(input("1. create a priority queue from queue import \n2. create a priority queue using a dictionary "))
    if user_in == 1:
        #using the queue import to access the priority queue functions
        pq = queue.PriorityQueue()

        pq.put((4, "Rathalos"))
        pq.put((3, "Lacriacus"))
        pq.put((5, "Rathian"))

        print(pq.get())
    elif user_in == 2:

        priority_keys = [1,2,3,4,5]
        
        monsters = {3: "Lacriacus", 1: "Lagombi", 4: "Rathalos", 5: "Rathian"}
        monster_items = monsters.items()

        print(sorted(monster_items))

        for i in range(len(priority_keys)):
            try:
                print(monsters.pop(priority_keys[i]))
            except KeyError:
                print("no key found")


        


def main():
    user_in= int(input("1. create a regular queue \n2. create a priority queue "))

    match user_in:
        case 1:
            reg_queue()
        case 2:
            prio_queue()

if __name__ == '__main__':
    main()