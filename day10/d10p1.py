with open('d10p1.in') as f:
    adaptors = list(map(int,f.read().splitlines()))
    
adaptors.sort()
diff1=0
diff3=0
prev=0

for adaptor in adaptors:
    if((adaptor-prev)==3):
        diff3+=1
    elif((adaptor-prev)==1):
        diff1+=1
    prev=adaptor
diff3+=1

total = diff1*diff3
print(f"length:{len(adaptors)}")
print(f"1:{diff1} 3:{diff3} total:{diff1*diff3}")
