with open('d5p1.in') as f:
	lines = f.read().splitlines()

maxseats = 128*8+7

seats = [0]*maxseats

for ticket in lines:
	ticket = ticket.replace('F','0')
	ticket = ticket.replace('B','1')
	ticket = ticket.replace('L','0')
	ticket = ticket.replace('R','1')

	idnum = int(ticket,2)

	seats[idnum] = idnum

for i in range(maxseats):
	if(seats[i]==0 and seats[i-1]!=0 and seats[i+1]!=0):
		print(i)
		break
