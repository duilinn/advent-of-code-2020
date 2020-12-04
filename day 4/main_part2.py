import re
inputFile = open("input")

fullText = inputFile.read()
fullText = fullText.replace(" ", "\n")

fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
eyeColours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
passports = fullText.split("\n\n")

for i in range(len(passports)):
    passports[i] = passports[i].split("\n")

    for j in range(len(passports[i])):
        passports[i][j] = passports[i][j].split(":")
        
passports[-1].pop()

numberOfValidPassports = 0

for i in range(len(passports)):
    validFlags = 0
    
    for j in range(len(passports[i])):
        #print("passport = " + str(i) + ", field = " + str(j) + ", " + str(passports[i][j]))
        field = passports[i][j][0]
        data = passports[i][j][1]
        if field==fields[0] and int(data) >= 1920 and int(data) <= 2002:
            validFlags += 2**6
        if field==fields[1] and int(data) >= 2010 and int(data) <= 2020:
            validFlags += 2**5
        if field==fields[2] and int(data) >= 2020 and int(data) <= 2030:
            validFlags += 2**4
        if field==fields[3]:
            if (data[-2:]=="cm" and int(data[:-2]) >= 150 and int(data[:-2]) <= 193) \
               or (data[-2:]=="in" and int(data[:-2]) >= 59 and int(data[:-2]) <= 76):
                validFlags += 2**3
        if field==fields[4]:
            reg = re.compile("^#[0-9a-f]{6}$")
            if reg.match(data):
                validFlags += 2**2
        if field==fields[5] and data in eyeColours:
            validFlags += 2**1
        if field==fields[6]:
            reg = re.compile("^[0-9]{9}$")
            if reg.match(data) :
                validFlags += 2**0

    #print("validFlags = " + str(validFlags))
            
    if validFlags == 127:
        numberOfValidPassports += 1


print(" number of valid passports = " + str(numberOfValidPassports))
