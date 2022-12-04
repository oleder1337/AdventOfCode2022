def getValue(deviation):
    upper=deviation.isupper()
    if upper:
        postAtt=26
    else:   
        postAtt=0
    deviation=deviation.lower()

    import string
    points=string.ascii_lowercase.index(deviation)+postAtt+1
    return points

def solveStack(stack):
    stack.sort(key=len)
    print(stack)
    for i in stack[2]:
        if i in stack[1] and i in stack[0]:
            deviation=getValue(i)
            return deviation



with open('input.txt',"r") as f:
    cont=f.read()

cont=cont.split('\n')
points=0
stack=[]
for index, i in enumerate(cont):
    print(i)
    print(index)
    stack.append(i)
    
    if (index+1)%3==0:
        
        print(stack)
        deviation=solveStack(stack)
        points=points+deviation
        
        stack=[]
    
        

    
       
    

        
        
        
        
                
print(points)

    