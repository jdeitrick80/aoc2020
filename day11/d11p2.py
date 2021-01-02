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
adj_seats= [[0]*(cols+2) for i in range(rows+2)]
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
                adj_seats[r][c]=0
                for i in range(c-1,0,-1):
                    if(seats_init[r][i]):
                        adj_seats[r][c]+=prev[r][i]
                        break
                for i in range(c+1,cols+1):
                    if(seats_init[r][i]):
                        adj_seats[r][c]+=prev[r][i]
                        break
                for j in range(r-1,0,-1):
                    if(seats_init[j][c]):
                        adj_seats[r][c]+=prev[j][c]
                        break
                for j in range(r+1,rows+1):
                    if(seats_init[j][c]):
                        adj_seats[r][c]+=prev[j][c]
                        break
                for i,j in zip(range(c-1,0,-1),range(r-1,0,-1)):
                    if(seats_init[j][i]):
                        adj_seats[r][c]+=prev[j][i]
                        break
                for i,j in zip(range(c-1,0,-1),range(r+1,rows+1)):
                    if(seats_init[j][i]):
                        adj_seats[r][c]+=prev[j][i]
                        break
                for i,j in zip(range(c+1,cols+1),range(r-1,0,-1)):
                    if(seats_init[j][i]):
                        adj_seats[r][c]+=prev[j][i]
                        break
                for i,j in zip(range(c+1,cols+1),range(r+1,rows+1)):
                    if(seats_init[j][i]):
                        adj_seats[r][c]+=prev[j][i]
                        break
                if(prev[r][c]==1 and adj_seats[r][c]>=5):
                    cur[r][c]=0
                elif(prev[r][c]==0 and adj_seats[r][c]==0):
                    cur[r][c]=1
    if(functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, cur, prev), True)):
        break
    else:
        count+=1
print(count)
print(sum(sum(cur,[])))

