class binheap:
    def __init__(self):
        self.heapList=[0]
        self.currentSize=0
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize+=1
        self.__percUp(self.currentSize)
    def __percUp(self,i):
        while i//2:
            if self.heapList[i]<self.heapList[i//2]:
                self.heapList[i],self.heapList[i//2]\
                    =self.heapList[i//2],self.heapList[i]
            i//=2
    def minChild(self,i):
        if i*2+1>self.currentSize:
            return i*2
        else:
            if self.heapList[i*2]<self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
    def delMin(self):
        retval=self.heapList[1]
        self.heapList[1]=self.heapList[self.currentSize]
        self.currentSize-=1
        self.heapList.pop() 
        self.__percDown(1)
        return retval
    def __percDown(self,i):
        while(i*2)<=self.currentSize:
            mc=self.minChild(i)
            if self.heapList[i]>self.heapList[mc]:
                self.heapList[i],self.heapList[mc]=\
                    self.heapList[mc],self.heapList[i]
            i=mc
    def buildHeap(self,alist):
        i=len(alist)//2
        self.currentSize=len(alist)
        self.heapList=[0]+alist[:]
        print(len(self.heapList),i)
        while(i>0):
            print(self.heapList,i)
            self.__percDown(i)
            i-=1
        print(self.heapList,i)
        return self.heapList
    
u=binheap()
u.buildHeap([34,5,8,90,13])