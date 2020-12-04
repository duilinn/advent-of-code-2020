inputFile = open("input")

fullText = inputFile.read()
fullText = fullText.replace(" ", "\n")

fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

passports = fullText.split("\n\n")

for i in range(len(passports)):
    passports[i] = passports[i].split("\n")

    for j in range(len(passports[i])):
        passports[i][j] = passports[i][j].split(":")


numberOfValidPassports = 0

for i in range(len(passports)):
    validFlags = 0
    
    for j in range(len(passports[i])):
        for k in range(7):
            if passports[i][j][0]==fields[k]:
                validFlags += 2**k

    if validFlags == 127:
        numberOfValidPassports += 1

print(passports[0][0][0])
print(" number of valid passports = " + str(numberOfValidPassports))
