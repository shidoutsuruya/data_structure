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
    def rotateRight(self,k):
        if not self.head:
            return self.head
        #getlength
        length,tail=1,self.head
        while tail.next:
            tail=tail.next
            length+=1
        k=k%length
        if k==0:
            return self.head
        #move tothe pivot
        cur=self.head 
        for i in range(length-k-1):
            cur=cur.next
        newhead,cur.next,tail.next=cur.next,None,self.head
        self.head=newhead
    def swapPairs(self):
        dummy=Node()
        pre,pre.next=dummy,self.head
        while pre.next and pre.next.next:
            cur=pre.next
            nxt=cur.next
            pre.next,nxt.next,cur.next=nxt,cur,nxt.next
            pre=cur
        self.head=dummy.next
    def reverseKGroup(self,k):
        dummy=jump=Node()
        dummy.next=l=r=self.head
        while True:
            count=0
            while r and count<k:
                r=r.next
                count+=1
            if count==k:
                pre,cur=r,l
                for _ in range(k):
                    cur.next,cur,pre=pre,cur.next,cur
                jump.next,jump,l=pre,l,r 
            else:
                self.head=dummy.next   
                return self.head    
    def removeDuplicates(self):
        dummy=pre=Node()
        cur=self.head 
        while cur and cur.next:
            if cur.val==cur.next.val:
                while cur and cur.next \
                    and cur.val==cur.next.val:
                    cur=cur.next
                cur=cur.next
                pre.next=cur
            else:
                pre=pre.next 
                cur=cur.next   
        self.head=dummy.next
    def deleteDuplicates(self):
        cur=self.head
        while cur:
            while cur.next and cur.next.val==cur.val:
                cur.next=cur.next.next
            cur=cur.next
    def partition(self,x):
        dummy1=l1=Node()
        dummy2=l2=Node()
        while self.head:
            if self.head.val<x:
                l1.next=self.head
                l1=l1.next
            else:
                l2.next=self.head
                l2=l2.next
            self.head=self.head.next
        l2.next=None
        l1.next=dummy2.next
        self.head=dummy1.next
    def reverseList(self):
        pre,cur=None,self.head
        while cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        self.head=pre
    def reverseBetween(self,left,right):
        if left==right:
            return self.head
        pre=dummy=Node()
        dummy.next=self.head
        for i in range(left-1):
            pre=pre.next
        #reverseList
        reverse,cur=None,pre.next 
        for i in range(right-left+1):
            nxt=cur.next
            cur.next=reverse
            reverse=cur
            cur=nxt
        #end reverse list
        pre.next,pre.next.next=cur,reverse
        return dummy.next
    @property
    def hasCycle(self):
        try:
            slow,fast=self.head,self.head.next
            while slow is not fast:
                slow=slow.next
                fast=fast.next.next
            return True
        except:
            return False
    def detectCycle(self):
        slow,fast=self.head,self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next 
            if slow==fast:
                break
        else:
            return None
        
        cur=self.head
        while cur!=fast:
            cur=cur.next
            fast=fast.next
        return cur
    def reorderList(self):
        if not self.head or not self.head.next:
            return self.head
        def _splitList(head):
            fast=slow=head 
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            middle=slow.next
            slow.next=None
            return head,middle
        def _reverseList(head):
            pre,cur=None,head
            while cur:
                nxt=cur.next
                cur.next=pre
                pre=cur
                cur=nxt
            return pre
        def _mergeLists(l1,l2):
            tail=head=l1 
            l1=l1.next
            while l2:
                tail.next=l2
                tail=tail.next
                l2=l2.next
                if l1:
                    l1,l2=l2,l1
            return head
        l1,l2=_splitList(self.head)
        l2=_reverseList(l2)
        self.head=_mergeLists(l1,l2)
    def insertSortList(self):
        pre=dummy=Node()
        cur=dummy.next=self.head
        while cur and cur.next:
            val=cur.next.val
            if cur.val<val:
                cur=cur.next
                continue 
            if pre.next.val>val:
                pre=dummy
            while pre.next.val<val:
                pre=pre.next
            new=cur.next
            cur.next=new.next
            new.next=pre.next
            pre.next=new
        self.haed=dummy.next
    def SortList(self):
        self.head=Tools.SortList(self.head)
    def isPalindrome(self):
        rev=None
        slow=fast=self.head
        while fast and fast.next:
            fast=fast.next.next 
            rev,rev.next,slow=slow,rev,slow.next  
        if fast:
            slow=slow.next 
        while rev and rev.val==slow.val:
            slow=slow.next 
            rev=rev.next 
        return not rev
    def oddEvenList(self):
        dummy1=odd=Node()
        dummy2=even=Node()
        while self.head:
            odd.next=self.head
            even.next=self.head.next
            odd=odd.next
            even=even.next 
            if even:
                self.head=self.head.next.next 
            else:
                self.head=None
        odd.next=dummy2.next
        self.head=dummy1.next
    def splitListToParts(self,k):
        #count num
        length=0
        cur=self.head
        while cur:
            length+=1
            cur=cur.next
        #divide into several list,return node
        ans=[None for _ in range(k)]
        l,r=divmod(length,k)
        pre=None
        for i in range(k):
            ans[i]=self.head
            for j in range(l+(1 if r>0 else 0)):
                pre=self.head
                self.head=self.head.next
            if pre:
                pre.next=None
            r-=1
        #show lists in list
        all_lst=[]
        for head in ans:
            lst=[]
            while head:
                lst.append(head.val)
                head=head.next
            all_lst.append(lst)
        return all_lst
            
        
                
        
class Tools():  
    @staticmethod  
    def py_list(head):
        lst=[]
        cur=head
        while cur:
            lst.append(cur.val)
            cur=cur.next
        return lst
    @staticmethod  
    def addTwoNumbers_reverse(l1,l2):
        carry=0
        cur=dummy=Node()
        while l1 or l2 or carry:
            v1=v2=0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            cur.next = Node(val)
            cur = cur.next
        return dummy.next      
    @staticmethod
    def mergeTwoLists(l1,l2):
        cur=dummy=Node(0)
        while l1 and l2:
            if l1.val<l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        cur.next=l1 or l2
        return dummy.next
    @staticmethod
    def mergeKLists(lists):
        if len(lists)==0:
            return None 
        elif len(lists)==1:
            return lists[0]
        else:
            output=lists[0]
        for i in range(1,len(lists)):
            output=Tools.mergeTwoLists(output,lists[i])
        return output
    @staticmethod
    def SortList(head):
        if not head or not head.next:
            return head
        pre,slow,fast=None,head,head
        while fast and fast.next:
            pre,slow,fast=slow,slow.next,fast.next.next
        pre.next=None
        return Tools.mergeTwoLists(Tools.SortList(head),Tools.SortList(slow))    
    @staticmethod
    def getInteresectionNode(l1,l2):
        if l1 is None or l2 is None:
            return None
        cur1=l1  
        cur2=l2   
        while cur1 is not cur2:
            if cur1:
                cur1=cur1.next
            else:
                cur1=l2
            if cur2:
                cur2=cur2.next
            else:
                cur2=l1
        return l1
    @staticmethod
    def addTwoNumbers(l1,l2):
        num1=num2=0
        while l1:
            num1=num1*10+l1.val
            l1=l1.next
        while l2:
            num2=num2*10+l2.val
            l2=l2.next
        sum_=num1+num2
        dummy=head=Node()
        if sum_==0:
            return head
        while sum_>0:
            head.next=Node(sum_%10)
            head=head.next
            sum_//=10
        #reverse answer
        pre=None
        cur=dummy.next
        while cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        return pre
        
if __name__ == '__main__':
    test=LinkedList()
    test2=LinkedList()
    for i in [1,2,3,4,5]:
        test.append(i)
        test2.append(i)
    lst=test.splitListToParts(3)
    print(lst)
    test.display()
    