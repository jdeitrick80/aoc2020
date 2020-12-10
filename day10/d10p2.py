with open('d10p1.in') as f:
    adaptors = list(map(int,f.read().splitlines()))
    
adaptors.sort()
diff1=0
diff3=0
prev=0
#if consecutive1s==1 combinations are 1
#if consecutive1s==2 combinations are 2
#if consecutive1s==3 combinations are 4
#if consecutive1s==4 combinations are 7
consecutive1s=0
cadapt=[0]
combinations=1

for adaptor in adaptors:
    if((adaptor-prev)==3):
        diff3+=1
        if(consecutive1s>1 and consecutive1s<4):
            combinations*=2*(consecutive1s-1)
        elif(consecutive1s==4):
            combinations*=7
        consecutive1s=0
        cadapt=[adaptor]
    elif((adaptor-prev)==1):
        diff1+=1
        consecutive1s+=1
        cadapt.append(adaptor)
    else:
        print("Jump that is not 1 or 3")
    prev=adaptor
if(consecutive1s>1 and consecutive1s<4):
    combinations*=2*(consecutive1s-1)
elif(consecutive1s==4):
    combinations*=7
diff3+=1

total = diff1*diff3
print(f"length:{len(adaptors)}")
print(f"1:{diff1} 3:{diff3} total:{diff1*diff3} combinations:{combinations}")
