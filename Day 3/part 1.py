with open('input.txt',"r") as f:
    cont=f.read()

cont=cont.split('\n')
points=0
for i in cont:
    
    if len(i)%2==0:
        halfIndex=int(len(i)/2)
        first=i[0:halfIndex]
        second=i[halfIndex:len(i)]
       
        for i in first:
            if i in second:
                deviation=i
                break

        
        upper=deviation.isupper()
        if upper:
            postAtt=26
        else:   
            postAtt=0
        print('Das die Deviation vor Standard: '+deviation)
        deviation=deviation.lower()

        import string
        points=points+string.ascii_lowercase.index(deviation)+postAtt+1
        
        
                
print(points)

    