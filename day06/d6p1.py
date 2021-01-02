with open('d6p1.in') as f:
    groups = f.read().split('\n\n')

total = 0

for group in groups:
    group = group.replace('\n','')
    #https://stackoverflow.com/questions/45773990/python-list-of-strings-to-list-of-unique-characters/45774130
    unique = list({c for word in group for c in word})
    total += len(unique)

print(total)
