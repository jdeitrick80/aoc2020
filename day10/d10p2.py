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
#if consecutive1s==n combinations are n(n-1)/2+1

consecutive1s=0
cadapt=[0]
combinations=1

for adaptor in adaptors:
    if((adaptor-prev)==3):
        diff3+=1
        combinations*=consecutive1s*(consecutive1s-1)/2+1
        consecutive1s=0
        cadapt=[adaptor]
    elif((adaptor-prev)==1):
        diff1+=1
        consecutive1s+=1
        cadapt.append(adaptor)
    prev=adaptor
combinations*=consecutive1s*(consecutive1s-1)/2+1
diff3+=1

total = diff1*diff3
print(f"length:{len(adaptors)}")
print(f"1:{diff1} 3:{diff3} total:{diff1*diff3} combinations:{int(combinations)}")
