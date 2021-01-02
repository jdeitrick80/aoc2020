import re

with open('d4p1.in') as f:
	passports = f.read().split('\n\n')

valid = 0
for passport in passports:
  byr = re.search(r'\bbyr:(\d{4})',passport)
  if(byr and int(byr[1])>=1920 and int(byr[1])<=2002):
    iyr = re.search(r'\biyr:(\d{4})',passport)
    if(iyr and int(iyr[1])>=2010 and int(iyr[1])<=2020):
      eyr = re.search(r'\beyr:(\d{4})',passport)
      if(eyr and int(eyr[1])>=2020 and int(eyr[1])<=2030):
        hgt = re.search(r'\bhgt:(\d+)(\w{2})',passport)
        if(hgt and ((hgt[2]=='in' and int(hgt[1])>=59 and int(hgt[1])<=76) or (hgt[2]=='cm' and int(hgt[1])>=150 and int(hgt[1])<=193))):
          hcl = re.search(r'\bhcl:(#[0-9a-f]{6,6})',passport)
          if(hcl):
            ecl = re.search(r'\becl:(amb|blu|brn|gry|grn|hzl|oth)\b',passport)
            if(ecl):
              pid = re.search(r'\bpid:(\d{9})\b',passport)
              if(pid):
                valid += 1

print(valid)
