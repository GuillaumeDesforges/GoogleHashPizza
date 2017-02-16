"""
def main(n):
    i=0
    while(i<n):
    """

import random

linetemp = []

name = "example"

i = 0

M = 0
T = 0

RCLH = []

cases = []

map = []

f = open("../assets/" + name + ".in", "r")
map0 = f.readlines()
for line in map0:
    if i == 0:
        for t in line:
            if t != " " and t != "\n":
                print type(int(t))
                RCLH += [int(t)]

    else:
        for t in line:
            if t != "\n" and t != "n":
                if t == "T":
                    linetemp += [1]
                    T += 1
                if t == "M":
                    linetemp += [-1]
                    M += 1
        map += [linetemp]
        linetemp = []
    i += 1
print(map)
print(RCLH)

R = RCLH[0]
C = RCLH[1]
L = RCLH[2]
H = RCLH[3]








maplibre = []

for line in map:
    linetemp = []
    for t in line:
        linetemp += [0]
    maplibre += [linetemp]

print (maplibre)


# maplibre : 0 libre 1 testee comme depart 2 allouee








partposs0=[]    #liste des cases possibles dep de RCLH
p=1


for x in range(1,H+1):
    for y in range(1,H+1):
        if x*y<=H and x*y>=2*L:
            partposs0+=[[[x,y],p]]

print(partposs0)










def essai():
    l = 0

    partposs=partposs0

    casef=[]
    corners = [[[0, 0], 0], [[0, C - 1], 0], [[R - 1, 0], 0], [[R - 1, C - 1], 0]]  # deuxieme chiffre, portee exploree

    nbc = 4  # nbre de corners restant a checker
    for i in range(4):
        case = corners[i][0]                                #initialisation
        for t in range(corners[i][1] + 1):
            cases += [[case[0] + t, case[1] + corners[i][1] - t]]
        casef+=[cases,i]      #casef [a][b}[0]   case b partant du a corner    casef[a][1] n corner

    test = 1

    while test == 1:
        i = randint(0, nbc -1)

        dx=-(i%2)*2+1
        if i<=1:
            dy=1
        else:
            dy=-1

        ncase=len(casef[i][0])
        j=randint(0,ncase-1)
        case = casef[i][j][0]

        casef[i]=casef[i][:j]+casef[i][j+1:]  #la case est viree de la liste d'attente
        if len(casef[i])==0:
            casef=casef[:i]+casef[i+1:]
            nbc-=1

        for i in range(len(partposs)):
            part=partposs[i]
            x=case[0]
            y=case[1]
            ok=1

            compo=0
            for xadd in range(part[0][0]):
                for yadd in range(part[0][1]):
                    if x+xadd*dx<0 or x+xadd*dx>=R or y+yadd*dy>=C or y+yadd*dy<0 :
                        ok=0      #On doit virer la part
                        break
                    if maplibre[x+xadd*dx][y+yadd*dy]==2:
                        ok=0
                        break
                    compo+=map[x+xadd*dx][y+yadd*dy]

                if ok==0:
                    break





