class Node:
    def __init__(self,init_data):
        self.data=init_data
        self.next=None 
    def getData(self):
        return self.data 
    def getNext(self):
        return self.next 
    def setData(self,newData):
        self.data=newData
    def setNext(self,newnext):
        self.next=newnext
        
class UnorderedList:
    def __init__(self):
        self.head=None
    def add(self,item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count
    def search(self,item):
        counter=0
        current=self.head
        found=False
        while current!=None and not found:
            counter+=1
            if current.getData()==item:
                found=True
                return counter
            else:
                current=current.next
        return found
    def remove(self,item):
        current=self.head
        previous=None 
        found=False
        while not found:
            if current.getData()==item:
                found=True
            else:
                previous=current
                current=current.getNext()
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())
        
    def order_search(self,item):
        current=self.head
        found=False
        stop=False
        while current!=None and not found and not Stop:
            if current.getData()==item:
                found=True
            else:
                if current.getData()>item:
                    stop=True
                else:
                    current=current.getNext()
        return found
    def order_add(self,item):
        current=self.head
        previous=None 
        stop=False
        while current!=None and not stop:
            if current.getData()>item:
                stop=True
            else:
                previous=current
                current=current.getNext()
        temp=Node(item)
        if previous==None:
            temp.setNext(self.head)
            self.head=temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
        
        
        
if __name__ == '__main__':
    test=UnorderedList()
    test.add(9)
    test.add(7)
    test.add(4)
    test.add(3)
    print(test.search(9))
     