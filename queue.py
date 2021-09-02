import random
class Queue():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[] 
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    
def hotpotato(namelist,num):
    q=Queue()
    for name in namelist:
        q.enqueue(name)
    print(q.items)
    while q.size()>1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue() 
    return q.dequeue()

class Printer:
    def __init__(self,ppm):
        self.pagerate=ppm 
        self.currentTask=None 
        self.timeRemaining=0 
    def tick(self):
        if self.currentTask!=None:
            self.timeRemaining-=1
            print('time remain:',self.timeRemaining)
            if self.timeRemaining<=0:
                print("finish,now no any tasks.")
                self.currentTask=None 
    def busy(self):
        if self.currentTask!=None:
            return True
        else:
            return False
    def startNext(self,newtask):
        self.currentTask=newtask
        self.timeRemaining=newtask.getPages()*60/self.pagerate
class Task:
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randrange(1,21)
    def getStamp(self):
        return self.timestamp
    def getPages(self):
        return self.pages
    def waitTime(self,currentTime):
        return currentTime-self.timestamp
def newPrintTask():
    num=random.randrange(1,181) #1/180 produce homework
    if num==180:
        return True
    else:
        return False
def simulation(numSeconds,pagesPerMinute):
    labprinter=Printer(pagesPerMinute)
    printQueue=Queue()
    waitingtimes=[]
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task=Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.busy()) and(not printQueue.isEmpty()):
            nexttask=printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()
    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("averagewait %6.2f s,%3d tasks remaining."%(averageWait,printQueue.size()))

if __name__ == '__main__':
    simulation(3600,5)

    
