import re

with open('d8p1.in') as f:
    program = f.read().splitlines()
    
acc=0
pc=0
inf_detect=[0]*len(program)
while(1):
    if(inf_detect[pc]):
        print(f"Loop Detected at PC:{pc} Prior ACC:{acc}")
        break
    else:
        inf_detect[pc]+=1
    inst = re.search(r'(\w+)\s([-+\d]+)',program[pc])
    if(inst and inst[1]=='nop'):
        pc+=1
    elif(inst and inst[1]=='acc'):
        acc+=int(inst[2])
        pc+=1
    elif(inst and inst[1]=='jmp'):
        pc+=int(inst[2])
