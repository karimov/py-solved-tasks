from queue import Queue
import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate



class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):
        return currentTime - self.timestamp


def simulation(numSeconds, pagePerMinute, numStudents):

    labprinter = Printer(pagePerMinute)
    printQueue = Queue()
    waitingTimes = []
    avTaskpTime = numSeconds // numStudents

    for currentSecond in range(numSeconds):

        if newPrintTask(avTaskpTime):
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingTimes.append(nextTask.waitTime(currentSecond))
            labprinter.startNext(nextTask)

        labprinter.tick()

    averageWait = sum(waitingTimes)/len(waitingTimes)
    print("Average Wait %6.2f secs and %3d tasks remaining, %3d tasks are printed" %(averageWait, printQueue.size(), len(waitingTimes)))

def newPrintTask(avTaskpTime):
    num = random.randrange(1, avTaskpTime + 1)
    if num == avTaskpTime:
        return True
    else:
        return False

#for i in range(10):
#    simulation(3600, 5)


