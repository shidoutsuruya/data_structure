class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
    def __setitem__(self, key, item):
        self.put(key,item)
    def __getitem__(self,key):
        return self.get(key)
    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root=TreeNode(key,val)
        self.size+=1
    def _put(self,key,val,currentNode):
        if key<currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild=TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild=TreeNode(key,val,parent=currentNode)
    def get(self,key):
        if self.root:
            res=self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key==key:
            return currentNode
        elif key<currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
    #avl
    def _put_avl(self,key,val,currentNode):
        if key<currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild=TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild=TreeNode(key,val,parent=currentNode)
    def updateBalance(self,node):
        if node.balanceFactor>1 or node.balanceFactor<-1:
            self.rebalance(node)
            return
        if node.parent!=None:
            if node.isLeftChild():
                node.parent.balanceFactor+=1
            elif node.rightChild():
                node.parent.balanceFactor-=1
            if node.parent.balanceFactor!=0:
                self.updateBalance(node.parent)
    def rotateLeft(self,rotRoot):
        newRoot=rotRoot.rightChild
        rotRoot.rightChild=newRoot.leftChild
        if newRoot.leftChild!=None:
            newRoot.leftChild.parent=rotRoot
        if rotRoot.isRoot():
            self.root=newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild=newRoot
            else:
                rotRoot.parent.rightChild=newRoot
        newRoot.leftChild=rotRoot
        rotRoot.parent=newRoot
        rotRoot.balanceFactor=rotRoot.balanceFactor+\
            1-min(newRoot.balanceFactor,0)
        rotRoot.balanceFactor=newRoot.balanceFactor+\
            1+max(rotRoot.balanceFactor,0)
    def rotateRight(self,rotRoot):
        newRoot=rotRoot.leftChild
        rotRoot.leftChild=newRoot.rightChild
        if newRoot.rightChild!=None:
            newRoot.rightChild.parent=rotRoot
        if rotRoot.isRoot():
            self.root=newRoot
        else:
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild=newRoot
            else:
                rotRoot.parent.leftChild=newRoot
        newRoot.rightChild=rotRoot
        rotRoot.parent=newRoot
        rotRoot.balanceFactor=rotRoot.balanceFactor+\
            1-min(newRoot.balanceFactor,0)
        rotRoot.balanceFactor=newRoot.balanceFactor+\
            1+max(rotRoot.balanceFactor,0)
     
    def rebalance(self,node):
        if node.balanceFactor<0:
            if node.rightChild.balanceFactor>0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor>0:
            if node.leftChild.balanceFactor:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)
            
                
                 
             
    
    
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key=key
        self.payload=val
        self.leftChild=left
        self.rightChild=right
        self.parent=parent
    def hasLeftChild(self):
        return self.leftChild
    def hasRightChild(self):
        return self.rightChild
    def isLeftChild(self):
        return self.parent and self.parent.leftChild==self
    def isRightChild(self):
        return self.parent and self.parent.rightChild==self
    def isRoot(self):
        return not self.parent
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    def replaceNodeData(self,key,value,lc,rc):
        self.key=key
        self.payload=value
        self.leftChild=lc
        self.rightChild=rc
        if self.hasLeftChild():
            self.leftChild.parent=self
        if self.hasRightChild():
            self.rightChild.parent=self
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem
    
    
        
if __name__=='__main__':
    mytree=BinarySearchTree()
    mytree[2]='hello'
    mytree[4]='john'
  