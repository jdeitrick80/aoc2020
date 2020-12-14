import re

with open('d12p1.in') as f:
    instructions = f.read().splitlines()

#   N
# W   E
#   S
#N==0 E==1 S==2 W==3
keyDir=['N','E','S','W']
ship = [0,0]
wp = [10,1]
shipDir = 1
xm=[1,1,-1,-1]
ym=[1,-1,-1,1]

for i in instructions:
    inst = re.search(r'([A-Z])(\d+)$', i)
    if(inst):
        if(inst[1]=='F'):
            ship[0]+=wp[0]*int(inst[2])
            ship[1]+=wp[1]*int(inst[2])
        elif(inst[1]=='R'):
            wp = wp[int((int(inst[2])/90)%2):]+wp[:int((int(inst[2])/90)%2)]
            wp[0]=abs(wp[0])*xm[int((int(inst[2])/90)%4)]
            wp[1]=abs(wp[1])*ym[int((int(inst[2])/90)%4)]
        elif(inst[1]=='L'):
            wp = wp[int((int(inst[2])/90)%2):]+wp[:int((int(inst[2])/90)%2)]
            wp[0]=abs(wp[0])*xm[-(int((int(inst[2])/90)%4))]
            wp[1]=abs(wp[1])*ym[-(int((int(inst[2])/90)%4))]
        elif(inst[1]=='N'):
            wp[1]+=int(inst[2])
        elif(inst[1]=='S'):
            wp[1]-=int(inst[2])
        elif(inst[1]=='E'):
            wp[0]+=int(inst[2])
        elif(inst[1]=='W'):
            wp[0]-=int(inst[2])

        if(wp[0]>0 and wp[1]>0):
            xm=[1,1,-1,-1]
            ym=[1,-1,-1,1]
        elif(wp[0]>0 and wp[1]<0):
            xm=[1,-1,-1,1]
            ym=[-1,-1,1,1]
        elif(wp[0]<0 and wp[1]<0):
            xm=[-1,-1,1,1]
            ym=[-1,1,1,-1]
        elif(wp[0]<0 and wp[1]>0):
            xm=[-1,1,1,-1]
            ym=[1,1,-1,-1]

print((abs(ship[0])+abs(ship[1])))
