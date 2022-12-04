with open('input.txt',"r") as f:
    cont=f.read()



#NOTES:
# A:ROCK 1P
#B:PAPER 2P
#C:SCISSORS 3P
#X:loose 1P +1
#Y:draw 2P
#Z:win 3P -1
# WIN:6P
# LOOSE: 0P 
# DRAW 3P


transdict={
    'X':0,
    'Y':3,
    'Z':6
}

#Syntax: draw/loose/win
trans=['Y','X','Z']

#Syntax: draw/loose/win
winmap={
    
    'A':[1,3,2],
    'B':[2,1,3],
    'C':[3,2,1]

}

cont=cont.split('\n')
points=0


for index, i in enumerate(cont):
    
    i=i.split(' ')
    roundpoints=winmap[i[0]][trans.index(i[1])]+transdict[i[1]]
    points=points+roundpoints

print('')
print(points)
    

