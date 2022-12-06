with open('input.txt',"r") as f:
    cont=f.read()

def check(char):
    s=char
    s = list(dict.fromkeys(s))
    if len(s)>13:
        print(s)
        return True
    else:
        return False


char=[]
for index,i in enumerate(cont):
    if len(char)==14:
        print(char)
        
        if check(char):
            print(index)
            break
        else:
            char.pop(0)
    
    char.append(i)

