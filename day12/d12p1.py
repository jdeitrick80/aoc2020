import re

with open('d12p1.in') as f:
    instructions = f.read().splitlines()

#   N
# W   E
#   S
#N==0 E==1 S==2 W==3
keyDir=['N','E','S','W']
ship = [0,0]
shipDir = 1

for i in instructions:
    inst = re.search(r'([A-Z])(\d+)$', i)
    if(inst):
        ins = ['X',inst[1],inst[2]]
        if(ins[1]=='F'):
            ins[1]=keyDir[shipDir]

        if(ins[1]=='R'):
            shipDir = (shipDir+int((int(ins[2])/90)))%4
            ins[1]=keyDir[shipDir]
        elif(ins[1]=='L'):
            shipDir = (shipDir-int((int(ins[2])/90)))%4
            ins[1]=keyDir[shipDir]
        elif(ins[1]=='N'):
            ship[1]+=int(ins[2])
        elif(ins[1]=='S'):
            ship[1]-=int(ins[2])
        elif(ins[1]=='E'):
            ship[0]+=int(ins[2])
        elif(ins[1]=='W'):
            ship[0]-=int(ins[2])

        print(f"{inst[1]}  {inst[2]} {ins[1]}  {ins[2]}  {ship} {keyDir[shipDir]}")

print((abs(ship[0])+abs(ship[1])))
