class BinaryTree:
    def __init__(self,root):
        self.key=root
        self.left=None
        self.right=None
    def insertLeft(self,newNode):
        if self.left==None:
            self.left=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.left=self.left
            self.left=t
    def insertRight(self,newNode):
        if self.right==None:
            self.right=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.right=self.right
            self.right=t
    def getright(self):
        return self.right
    def getleft(self):
        return self.left
    def setRootVal(self,obj):
        self.key=obj
    def getRootVal(self):
        return self.key
    def preorder(self):
        print(self.key)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key)   
        if self.right:
            self.right.inorder()
    def postorder(self):
        if self.left:
            self.left.postorder()      
        if self.right:
            self.right.postorder()
        print(self.key)
        
        
tree=BinaryTree(4)
for i,j in zip([2,3,4],[8,4,6]):
    tree.insertLeft(i)
    tree.insertRight(j)
    
tree.inorder()