with open('d6p1.in') as f:
    groups = f.read().split('\n\n')

total = 0

for group in groups:
    indvs = group.splitlines()
    common = indvs[0]
    for indv in indvs:
        #https://www.sanfoundry.com/python-program-check-common-letters-string/
        common=list(set(indv)&set(common))

    total += len(common)

print(total)
