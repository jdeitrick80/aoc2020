import re

with open('d7p1.in') as f:
    rules = f.read().splitlines()
count = 0
allbags = []
bags = ['1 shiny gold bag']
while(bags):
    bag = bags.pop()
    bagmatch = re.search(r'(\d+)\s([\w\s]+)\sbag',bag)
    if(bagmatch):
        bag = bagmatch[2]
        mult = bagmatch[1]
    for rule in rules:
        match = re.search(rf'{bag}[\w\s]+contain\s([\s\w,]+)\.',rule)
        if(match):
            innerbags = match[1].split(',')
            for innerbag in innerbags:
                innermatch = re.search(r'(\d+)\s([\w\s]+\sbag)',innerbag)
                if(innermatch):
                    count += (int(innermatch[1])*int(mult))
                    bags.append((str(int(innermatch[1])*int(mult)))+" "+innermatch[2])
print(count)
