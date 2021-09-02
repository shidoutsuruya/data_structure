def binarySearch(alist:list,item:int):
    "return:bool"
    first=0
    last=len(alist)-1
    found=False
    while first<=last and not found:
        midpoint=(first+last)//2
        if alist[midpoint]==item:
            found=True 
        else:
            if item<alist[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1
    return found

def binarySearch2(alist,item):
    if len(alist)==0:
        return False
    else:
        midpoint=len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch2(alist[:midpoint],item)
            else:
                return binarySearch2(alist[midpoint+1:],item)
            
def bubbleSort(alist):
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
    return alist
                
def selectionSort(alist):
    for  i in range(len(alist)-1,0,-1):
        positionOfMax=0
        for j in range(1,i+1):
            if alist[j]>alist[positionOfMax]:
                positionOfMax=j
        alist[i],alist[positionOfMax]=alist[positionOfMax],alist[i]
    return alist
        
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue=alist[index]
        position=index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position-=1
        alist[position]=currentvalue
    return alist

def shellSort(alist):
    sublistCount=len(alist)//2
    while sublistCount>0:
        for i in range(sublistCount):
            gapInsertionSort(alist,i,sublistCount)
        print("after increment of size:",sublistCount,"the list is",alist)
        sublistCount//=2
    return alist
    
def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue=alist[i]
        position=i
        
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position-=gap
            
        alist[position]=currentvalue
def mergeSort(lst):
    if len(lst)<=1:
        return lst
    middle=len(lst)//2
    left=mergeSort(lst[:middle])
    right=mergeSort(lst[middle:])
    
    merged=[]
    while left and right:
        if left[0]<=right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged

def quickSort(alist,first=0,last=9):
    first=0
    last=len(alist)-1
    if first<last:
        splitpoint=partition(alist,first,last)
        quickSort(alist,first,splitpoint-1)
        quickSort(alist,splitpoint+1,last)
    return alist
        
def partition(alist,first,last):
    pivotvalue=alist[first]
    leftmark=first+1
    rightmark=last
    done=False 
    while not done:
        while leftmark<=rightmark and alist[leftmark]<=pivotvalue:
            leftmark+=1
        while alist[rightmark]>=pivotvalue and rightmark>=leftmark:
            rightmark-=1
        if rightmark<leftmark:
            done=True
        else:
            alist[leftmark],alist[rightmark]=alist[rightmark],alist[leftmark]
    return rightmark
            
print(quickSort([2,4,5,6,2,3]))