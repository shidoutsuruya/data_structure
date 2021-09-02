import operator
class tree():
    def __init__(self,root):
        self.root=[root,[],[]]
    def insertLeft(self,newBranch):
        t=self.root.pop(1)
        if len(t)>1:
            self.root.insert(1,[newBranch,t,[]])
        else:
            self.root.insert(1,[newBranch,[],[]])
        return self.root
    def insertRight(self,newBranch):
        t=self.root.pop(2)
        if len(t)>1:
            self.root.insert(2,[newBranch,[],t])
        else:
            self.root.insert(2,[newBranch,[],[]])
        return self.root
    def getRootVal(self):
        return self.root[0]
    def setRootVal(self,newVal):
        self.root[0]=newVal
    def getLeftChild(self):
        return self.root[1]
    def getRightChild(self):
        return self.root[2]

class BinaryTree:
    def __init__(self,root):
        self.key=root
        self.leftChild=None
        self.rightChild=None
    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t
    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t
    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def setRootVal(self,obj):
        self.key=obj
    def getRootVal(self):
        return self.key
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
    def inorder(self):
        if self.leftChild:
            self.leftChild.preorder()
        print(self.key)   
        if self.rightChild:
            self.rightChild.preorder()
    def postorder(self):
        if self.leftChild:
            self.leftChild.preorder()      
        if self.rightChild:
            self.rightChild.preorder()
        print(self.key)
class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
 
def buildParseTree(fpexp):
    fplist=list(fpexp)
    pStack=Stack()
    eTree=BinaryTree("")
    pStack.push(eTree)
    currentTree=eTree
    print(type(currentTree))
    for i in fplist:
        if i=='(':
            currentTree.insertLeft("")
            pStack.push(currentTree)
            currentTree=currentTree.getLeftChild()
        elif i not in ['+','-','*','/',')']:
            currentTree.setRootVal(int(i))
            parent=pStack.pop()
            currentTree=parent
        elif i in ['+','-','*','/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree=currentTree.getRightChild()
        elif i==")":
            currentTree=pStack.pop()
        else:
            raise ValueError
    return eTree

def evaluate(parseTree):
    opers={"+":operator.add,"-":operator.sub,
           "*":operator.mul,"/":operator.truediv}       
    leftC=parseTree.getLeftChild()
    rightC=parseTree.getRightChild()
    if leftC and rightC:
        fn=opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

def post_evaluate(tree):
    opers={"+":operator.add,"-":operator.sub,
           "*":operator.mul,"/":operator.truediv}    
    res1=None
    res2=None 
    if tree:
        res1=post_evaluate(tree.getLeftChild())
        res2=post_evaluate(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()
        

    
