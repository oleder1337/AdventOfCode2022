def getRange(s):
    s=s.split('-')
    t=range(int(s[0]),int(s[1])+1)
    return t

def checkContain(s):
    s.sort(key=len)
    for i in s[0]:
        if i not in s[1]:
            return 0
    return 1



with open('input.txt',"r") as f:
    cont=f.read()

    cont=cont.split('\n')
    res=0
    for i in cont:
        i=i.split(',')
        i=[getRange(i[0]),getRange(i[1])]
        res=res+checkContain(i)
    
print(res)
