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
    def removeElements(self,item):
        cur=dummy=Node()
        dummy.next=self.head
        while cur.next:
            if cur.next.val==item:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return dummy.next
    def removeNthFromEnd(self,index):
        dummy=Node()
        dummy.next=self.head
        fast = slow = self.head
        for _ in range(index):
            fast = fast.next
        if not fast:
            return dummy.next.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
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
   
                
             
class solution():  
    @staticmethod  
    def py_list(head):
        lst=[]
        cur=head
        while cur:
            lst.append(cur.val)
            cur=cur.next
        return lst
    @staticmethod  
    def addTwoNumbers(l1_node,l2_node):
        carry=0
        cur=dummy=Node()
        while l1_node or l2_node or carry:
            v1=v2=0
            if l1_node:
                v1 = l1_node.val
                l1_node = l1_node.next
            if l2_node:
                v2 = l2_node.val
                l2_node = l2_node.next
            carry, val = divmod(v1+v2+carry, 10)
            cur.next = Node(val)
            cur = cur.next
        return dummy.next      
    @staticmethod
    def mergeTwoLists(l1_node,l2_node):
        cur=dummy=Node(0)
        while l1_node and l2_node:
            if l1_node.val<l2_node.val:
                cur.next=l1_node
                l1_node=l1_node.next
            else:
                cur.next=l2_node
                l2_node=l2_node.next
            cur=cur.next
        cur.next=l1_node or l2_node
        return dummy.next
   
                
        
        
if __name__ == '__main__':
    test=LinkedList()
    test2=LinkedList()
    for i in [1,2,4,54]:
        test.append(i)
    for j in [3,7,8]:
        test2.append(j)
    new_head=solution.mergeTwoLists(test.head,test2.head)
    print(solution.hello(new_head))

    