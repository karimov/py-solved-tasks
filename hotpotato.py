from queue import Queue
import random

def hotPotato(nameList, num):
    simqueue = Queue()

    for name in nameList:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        num = random.randrange(14)
        simqueue.dequeue()
    return simqueue.dequeue()
