inputFile = open("input")

fullText = inputFile.read()

def getRowCol(rowCol):

    rowCol[0] = int(rowCol[0].replace("F","0").replace("B","1"),2)
    rowCol[1] = int(rowCol[1].replace("L","0").replace("R","1"),2)
    return rowCol

def getSeatId(rowCol):
    return (rowCol[0] * 8) + rowCol[1]
seatCodes = fullText.split("\n")
seatCodes.pop()

for i in range(len(seatCodes)):
    seatCodes[i] = getRowCol([seatCodes[i][:-3], seatCodes[i][-3:]])

seatIds = []

for i in range(len(seatCodes)):
    seatIds.append(getSeatId(seatCodes[i]))
    
print(max(seatIds))
print(min(seatIds))

for i in range(80,920):
    if i not in seatIds:
        print(i)
