import re

with open('d4p1.in') as f:
	passports = f.read().split('\n\n')

valid = 0
for passport in passports:
	if(re.search(r'\bbyr',passport) and
	re.search(r'\biyr',passport) and
	re.search(r'\beyr',passport) and
	re.search(r'\bhgt',passport) and
	re.search(r'\bhcl',passport) and
	re.search(r'\becl',passport) and
	re.search(r'\bpid',passport)):
		valid += 1

print(valid)



