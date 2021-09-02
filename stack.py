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
    
def parChecker(string):
    s=Stack()
    balance=True
    index=0
    while index<len(string) and balance:
        symbol=string[index]
        if symbol in "{([":
            s.push(symbol)
        else:
            if s.isEmpty():
                balance=False
            else:
                top=s.pop()
                if not matches(top,symbol):
                    balance=False
        index+=1 
    if balance and s.isEmpty():
        return True 
    else:
        return False
def matches(open,close):
    opens="([{"
    closers=")]}"
    return opens.index(open)==closers.index(close)
def baseCounter(decNumber,base):
    digits="0123456789ABCDEF"
    remstack=Stack()
    while decNumber>0:
        rem=decNumber%base
        remstack.push(rem)
        decNumber//=base
    newString=""
    while remstack.isEmpty()==False:
        newString+=digits[remstack.pop()]
    return newString
class compute_equation:
    def __init__(self):
        self.__doMath
    def infixToPostfix(self,equation):
        prec={}
        prec["*"]=3
        prec["/"]=3
        prec["+"]=2
        prec["-"]=2
        prec["("]=1
        opStack=Stack()
        postfixList=[]
        equation=equation.replace(" ", "")
        tokenList=list(equation)
        for token in tokenList:
            if token in  ''.join([chr(i) for i in (range(65,65+26))])\
            +''.join([chr(i) for i in (range(97,97+26))])+'0123456789':
                postfixList.append(token)
            elif token=="(":
                opStack.push(token)
            elif token==")": 
                topToken=opStack.pop()
                while topToken!='(':
                    postfixList.append(topToken)
                    topToken=opStack.pop()
            else:
                while(not opStack.isEmpty()) and \
                    (prec[opStack.peek()]>=prec[token]):
                        postfixList.append(opStack.pop())
                opStack.push(token)
        while not opStack.isEmpty():
            postfixList.append(opStack.pop())
        return "".join(postfixList)
    def postfixEval(self,postfixExpr:str):
        operandStack=Stack()
        tokenlist=list(postfixExpr)
        for token in tokenlist:
            if token in "0123456789":
                operandStack.push(int(token))
            else:
                operand2=operandStack.pop()
                operand1=operandStack.pop()
                result=self.__doMath(token,operand1,operand2)
                operandStack.push(result)
        return operandStack.pop()
    def __doMath(self,op,op1,op2):
        if op=='*':
            return op1*op2
        elif op=="/":
            return op1/op2
        elif op=='+':
            return op1+op2
        elif op=='-':
            return op1-op2
        else:
            print("error!!!")
        
if __name__=='__main__':
    u=compute_equation()
    

