with open('input.txt',"r") as f:
    cont=f.read()

def check(char):
    s=char
    s = list(dict.fromkeys(s))
    if len(s)>3:
        return True
    else:
        return False


char=[]
for index,i in enumerate(cont):
    if len(char)==4:
        
        if check(char):
            print(index)
            break
        else:
            char.pop(0)
    
    char.append(i)

