class Node:
    def __init__(self,init_val=None):
        self.val=init_val
        self.next=None 
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,item):
        temp=Node(item)
        temp.next=self.head
        self.head=temp
    def append(self,item):
        cur=self.head
        if cur==None: 
            self.head=Node(item)
        else:
            while cur.next:
                cur=cur.next
            cur.next=new=Node(item)
    def display(self):
        lst=[]
        cur=self.head
        while cur:
            lst.append(cur.val)
            cur=cur.next
        print(lst)
    @property
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.next
        return count
    def is_exist(self,item):
        counter=0
        current=self.head
        found=False
        while current!=None and not found:
            counter+=1
            if current.val==item:
                found=True
                return counter
            else:
                current=current.next
        return found
    def remove_203(self,item):
        cur=dummy=Node()
        dummy.next=self.head
        while cur.next:
            if cur.next.val==item:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return dummy.next
    def order_search(self,item):
        current=self.head
        found=False
        stop=False
        while current!=None and not found and not stop:
            if current.val==item:
                found=True
            else:
                if current.val>item:
                    stop=True
                else:
                    current=current.next
        return found
    def order_add(self,item):
        current=self.head
        previous=None 
        stop=False
        while current!=None and not stop:
            if current.val>item:
                stop=True
            else:
                previous=current
                current=current.next
        temp=Node(item)
        if previous==None:
            temp.next=self.head            
            self.head=temp
        else:
            temp.next=current
            previous.next=temp
   
                
                
        
        
        
if __name__ == '__main__':
    test=LinkedList()
    for i in [2,3,4,7,7,5,9]:
        test.append(i)
    test.remove_203(1)
    test.display()
    
    