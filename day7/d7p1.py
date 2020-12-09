import re

with open('d7p1.in') as f:
    rules = f.read().splitlines()
allbags = []
bags = ['shiny gold']
while(bags):
    bag = bags.pop()
    for rule in rules:
        match = re.search(rf'^([\w\s]+)bags\scontain.+{bag}',rule)
        if(match):
            allbags.append(match[1])
            bags.append(match[1])
print(len(set(allbags)))
