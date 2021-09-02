def listsum(numList):
    if len(numList)==1:
        return numList[0]
    else:
        return numList[0]+listsum(numList[1:])
    
def toStr(n,base):
    convertString="0123456789ABCDEF"
    if n<base:
        return convertString[n]
    else:
        return toStr(n//base,base)+convertString[n%base]
    
def moveTower(n,A,B,C):
    if n>=1:
        moveTower(n-1,A,C,B)
        moveDisk(n,A,C)
        moveTower(n-1,B,A,C)
def moveDisk(disk,A,C):
    print("move disk[{0}] from {1} to {2}".format(disk,A,C))
    

    
def recMC(coinValueList,change,knownResults):
    minCoins=change
    if change in coinValueList:
        knownResults[change]=1
        return 1
    elif knownResults[change]>0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMC(coinValueList,change-i,knownResults)
            if numCoins<minCoins:
                minCoins=numCoins
                knownResults[change]=minCoins
    return minCoins

def dpMakeChange(coinValueList,change,minCoins,coinUsed):
    for cents in range(1,change+1):
        coinCount=cents
        newCoin=1
        for j in [c for c in coinValueList if c<=cents]:
            if minCoins[cents-j]+1<coinCount:
                coinCount=minCoins[cents-j]+1
                newCoin=j
        minCoins[cents]=coinCount
        coinUsed[cents]=newCoin
    return minCoins[change],coinUsed

        
if __name__=='__main__':
    amnt=63
    clist=[1,5,10,21,25]
    coinUsed=[0]*(amnt+1)
    coinCount=[0]*(amnt+1) 
    print(dpMakeChange(clist,amnt,coinCount,coinUsed))