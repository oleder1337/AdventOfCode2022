with open("input.txt","r") as f:
    cont=f.read()

cont=cont.split('\n\n')
maxCal=[]
for i in cont:
    cal=0
    i=i.split('\n')
    for j in i:
        j=int(j)
        cal=cal+j
    

    maxCal.append(cal)  


maxCal.sort()
maxCal=maxCal[len(maxCal)-3:len(maxCal)]
summe=0
for i in maxCal:
    summe=summe+i


print(summe)



      

