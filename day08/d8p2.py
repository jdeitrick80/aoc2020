import re

with open('d8p1.in') as f:
    program = f.read().splitlines()
    
acc=0
pc=0
bug=0
delta=0
inf_detect=[0]*len(program)
while(1):
    if(pc>=len(program)):
        print(f"Program Complete ACC:{acc}")
        break
    if(inf_detect[pc]):
        print(f"Loop Detected at PC:{pc} Prior ACC:{acc} Bug Iteration: {bug}")
        pc = 0
        acc = 0
        inf_detect=[0]*len(program)
        bug += 1
        delta = 0
    else:
        inf_detect[pc]+=1
    inst = re.search(r'(\w+)\s([-+\d]+)',program[pc])
    if(inst and inst[1]=='nop'):
        delta+=1
        if(delta!=bug):
            pc+=1
        else:
            pc+=int(inst[2])
    elif(inst and inst[1]=='acc'):
        acc+=int(inst[2])
        pc+=1
    elif(inst and inst[1]=='jmp'):
        delta+=1
        if(delta!=bug):
            pc+=int(inst[2])
        else:
            pc+=1
