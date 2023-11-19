
def readTest():
    with open('testinput.txt','r') as f:
        cont=f.read()
        cont=cont.split('\n')
    return cont

def checkVisibility(map):
    height=len(map)
    width=len(map[0])
    for i in map:
        
        maxVal=max(i)
        for index,j in enumerate(i):
            if type(j) is not tuple:
                if j== maxVal:
                    i[index]=(j,True)
                else:
                    i[index]=(j,False)
            else:
                maxVal=maxVal[0]
                if j==maxVal:
                    j[1]=True
                
            
    return map

        

def rotate(map):
    height=len(map)
    width=len(map[0])
    treeMap=[]

    for i in range(0,width):
        row=[]
        for j in range(0,height):
            cur=map[j]
            cur=list(cur)
            row.append(cur[i])
        treeMap.append(row)
    return treeMap

def cleanUp(map):
    height=len(map)
    width=len(map[0])

    
    for rowNum,i in enumerate(map):
        if rowNum==0 or rowNum==height-1:
            border=True
        else:
            border=False
        for index,j in enumerate(i):
            if border==True:
                i[index]=True
            else:
                if type(i[index]) != bool:
                    i[index]=i[index][1]

            i[0]=True
            i[len(i)-1]=True

    for i in map:
        

    return map
            


def main():
    input=readTest()
    treeMap=[]
    for i in input:
        row=list(i)
        treeMap.append(row)

    treeMap=checkVisibility(treeMap)
    treeMap=rotate(treeMap)
    treeMap=checkVisibility(treeMap)
    treeMap=rotate(treeMap)
    treeMap=rotate(treeMap)
    treeMap=rotate(treeMap)
    treeMap=cleanUp(treeMap)


    
            
    
    
    
    
    print('\nResulting Forrest:\n')
    for i in treeMap:
        print(i)






if __name__=='__main__':
    main()

