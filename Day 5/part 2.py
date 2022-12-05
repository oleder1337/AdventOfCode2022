def formatCargo(cargo):
    cargo=cargo.split('\n')
    footer=cargo[len(cargo)-1]
    footer=footer.split(' ')
    footer=[x for x in footer if x!='']
    cargoMap={}
    for i in footer:
        cargoMap[i]=[]
    
    for index,line in enumerate(cargo):
   
        counter=0
        stack=1
        cur=''
        skip=False
    
        for i in line:
        
            if skip==True:
                
                skip=False
                continue
                

            cur=cur+i
            counter=counter+1
            if counter==3:
                if '[' in cur:
                    cur=cur.replace('[','')
                    cur=cur.replace(']','')
                    cargoMap[str(stack)].append(cur)
                stack=stack+1
                cur=''
                skip=True
                counter=0
    
    return cargoMap

def printAsPicture(cargo):
    def GetMaxFlow(flows):        
        maks=max(flows, key=lambda k: len(flows[k]))
        return len(flows[maks])
    tmp=[]
    maxLen=GetMaxFlow(cargo)

    counter=0
    grid=''
    for line in range(maxLen-1,-1,-1):
   
        for i in cargo:
       
            if len(cargo[i])-1-line>=0:
        
                try:
                    grid=grid+'['+str(cargo[i][len(cargo[i])-1-line])+']'
                except IndexError:
                    grid=grid+'   '
            else:
                grid=grid+'   '
            grid=grid+' '
        
        grid=grid+'\n'

    for i in cargo:
        grid=grid+' '+str(i)+'  '
            
            
    print(grid)



def move(amount,origin,goal,cargo):
    tmp=[]
    cargo[origin]
    for i in range(0,int(amount)):
    
        elem=cargo[origin].pop(0)
        tmp.append(elem)
    print(tmp)
    tmp.reverse()
    print(tmp)
    for elem in tmp:
        cargo[goal].insert(0,elem)
    return cargo


def formatCommands(command,cargo):
    
    #move x from y to z
    command=command.replace('move ','')
    command=command.replace(' from','')
    command=command.replace(' to','')
    command=command.split(' ')
    

    cargo=move(command[0],command[1],command[2],cargo)
    return cargo
    

with open('input.txt',"r") as f:
    cont=f.read()

cont=cont.split('\n\n')

cargo=cont[0]
moves=cont[1]
moves=moves.split('\n')
cargo=formatCargo(cargo)

for i in moves:
    printAsPicture(cargo)
    print('')   
    print(i)
    cargo=formatCommands(i,cargo)
    printAsPicture(cargo)
    print('')
    
  

result=''
for i in cargo:
    result=result+cargo[i][0]


print(result)
