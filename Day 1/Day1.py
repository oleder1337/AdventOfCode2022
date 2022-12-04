with open("input.txt","r") as f:
    cont=f.read()

cont=cont.split('\n\n')
maxCal=0
for i in cont:
    cal=0
    i=i.split('\n')
    for j in i:
        j=int(j)
        cal=cal+j
    

    if cal>maxCal:
        maxCal=cal




      

print(maxCal)