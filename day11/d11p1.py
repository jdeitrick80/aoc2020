import numpy as np
import functools
from copy import deepcopy

with open('d11p1.in') as f:
    seats=f.read().splitlines()

rows=len(seats)
cols=len(seats[0])
seats_init = [[0]*(cols+2) for i in range(rows+2)]
cur= [[0]*(cols+2) for i in range(rows+2)]
prev= [[0]*(cols+2) for i in range(rows+2)]
print(f"seats_init is {len(seats_init)} by {len(seats_init[0])}")
print(f"Seating area is {rows} by {cols}")
for row in range(rows):
    for col in range(cols):
        if(seats[row][col]=='L'):
            seats_init[row+1][col+1]=1

prev=[]
count=0


while(1):
    prev=deepcopy(cur)
    for r in range(1,rows+1):
        for c in range(1,cols+1):
            if(seats_init[r][c]==1):
                adj_seats=prev[r-1][c-1]+prev[r-1][c]+prev[r-1][c+1]+prev[r][c-1]+prev[r][c+1]+prev[r+1][c-1]+prev[r+1][c]+prev[r+1][c+1]
                if(prev[r][c]==1 and adj_seats>=4):
                    cur[r][c]=0
                elif(prev[r][c]==0 and adj_seats==0):
                    cur[r][c]=1
            #print(seats_cur[row][col],end="")
        #print("")
    if(functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, cur, prev), True)):
        break
    else:
        count+=1
print(count)
print(sum(sum(cur,[])))

