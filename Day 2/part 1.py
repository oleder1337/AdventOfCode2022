with open('input.txt',"r") as f:
    cont=f.read()



#NOTES:
# A:ROCK 1P
#B:PAPER 2P
#C:SCISSORS 3P
#X:loose 1P
#Y:draw 2P +1
#Z:win 3P +2
# WIN:6P
# LOOSE: 0P
# DRAW 3P




#Syntax: translate/Win/loose
transdict={
    'X':['A','C','B'],
    'Y':['B','A','C'],
    'Z':['C','B','A']
}

cont=cont.split('\n')
points=0
for index, i in enumerate(cont):
    print(i)
    i=i.split(' ')
    i[1]=transdict[i[1]]
    print(i)
    print(points)
    if i[1][0]=='A':
        points=points+1
    if i[1][0]=='B':     
        points=points+2
        print(points)
    if i[1][0]=='C':
        points=points+3
    if i[1][0]==i[0]:
        points=points+3  
    if i[1][1]==i[0]:
        points=points+6


    
    
print('')
print(points)
    

