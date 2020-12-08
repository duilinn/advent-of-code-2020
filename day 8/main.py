from copy import *
inputFile = """acc +37
acc -1
nop +512
acc +0
jmp +60
acc -3
nop +317
jmp +130
acc +22
acc +34
jmp +486
acc -18
nop +610
acc -14
nop +274
jmp +439
acc -6
acc -1
acc -4
acc +7
jmp +175
nop +179
jmp +197
jmp +76
acc -1
acc +24
jmp +472
acc +8
acc -15
acc +0
jmp +551
acc +46
acc +27
jmp +1
acc +45
jmp +153
acc +14
jmp +207
jmp +1
jmp +557
nop +424
jmp +571
nop -19
nop +9
acc +2
acc +29
jmp +14
acc -10
acc +43
acc +43
jmp +75
jmp +311
jmp +517
acc -6
acc +13
jmp +140
nop +348
acc +0
jmp +275
jmp +52
jmp +110
acc +11
acc +15
jmp +13
acc +7
jmp +216
jmp +174
nop +24
acc -16
acc +46
acc -17
jmp +519
acc -15
acc +46
acc -4
jmp +309
acc +14
acc +36
acc -15
jmp +244
acc +37
acc +43
jmp +146
jmp +260
jmp +217
acc +39
jmp +454
nop +16
nop +255
acc +31
jmp +13
acc +38
acc +45
acc +24
jmp +534
acc +13
acc +44
acc +34
jmp +286
jmp +1
acc -12
jmp -45
jmp +147
acc -2
acc +24
nop +391
acc +11
jmp +242
acc +1
acc +28
jmp +423
acc +5
jmp +319
acc +45
nop +350
acc +34
acc +7
jmp +47
nop +32
acc +2
acc +0
jmp +252
acc -4
acc +23
jmp +452
acc -5
acc +48
jmp -104
acc +38
jmp +172
acc +7
acc +31
jmp +5
acc +19
acc +12
acc +26
jmp +232
acc -12
nop +121
nop +80
acc +46
jmp +126
jmp +82
nop +69
jmp -128
acc +18
acc +45
acc +14
acc +45
jmp +219
jmp +422
acc +2
acc +40
acc +13
jmp +450
acc +48
jmp +172
acc +19
acc -10
jmp +69
nop +336
nop -6
jmp +265
jmp -136
jmp +350
acc +31
acc +39
nop +389
nop +404
jmp +16
acc +13
nop -41
acc -2
acc -14
jmp +159
jmp -111
acc +40
acc +36
acc -17
jmp -143
acc +36
acc +29
acc +19
acc +0
jmp +159
jmp +279
acc +31
jmp +346
acc +15
nop +173
acc +48
jmp -183
acc +16
acc +31
jmp +418
acc -13
jmp +280
acc +30
nop +229
jmp -139
acc +0
acc +9
jmp +354
acc +12
jmp +310
jmp -129
acc -8
jmp -96
acc -3
acc +1
jmp +51
jmp +303
acc +28
jmp -186
acc +36
acc -10
nop +72
nop +345
jmp +200
acc +6
acc -14
jmp +87
nop +318
jmp +273
nop +309
acc +50
jmp +147
jmp +387
acc +38
nop -169
acc +44
jmp +28
nop +208
nop +43
acc +26
acc -13
jmp -160
jmp +233
acc +22
jmp +357
jmp +374
acc -6
acc +38
jmp +100
jmp -36
acc +38
nop +330
acc +46
jmp -43
acc +34
nop +239
acc +45
acc +15
jmp +48
acc +49
acc +20
acc -5
acc +41
jmp +70
jmp +211
jmp +144
acc +29
acc +36
acc -15
jmp -24
jmp +1
jmp -17
acc -18
acc +27
acc +34
jmp -21
jmp +1
acc +35
acc -5
acc +24
jmp +337
nop -240
jmp +180
acc -1
nop +49
jmp +260
acc +40
acc +42
jmp -165
acc +31
acc +30
nop -234
jmp +27
acc +45
acc +48
acc +44
acc -19
jmp +70
acc +20
acc +18
jmp +219
acc +46
jmp -85
acc +43
acc +21
jmp -4
acc +37
acc +26
acc +16
jmp -257
acc +39
acc +7
jmp -260
acc +42
acc +10
acc +36
acc +47
jmp +2
jmp -249
acc +20
acc -1
acc +21
jmp +74
jmp +31
acc +32
jmp +64
acc +34
jmp -255
acc -8
acc -2
acc +26
jmp -102
jmp +229
acc -14
acc +25
jmp -154
acc -15
jmp -92
nop -37
acc -5
acc +50
acc +43
jmp +73
acc +1
acc -17
acc +19
acc +24
jmp -319
nop -225
jmp -304
acc +49
acc +5
acc -17
jmp +14
acc +42
acc -9
acc -10
acc +45
jmp -125
jmp -46
acc +13
acc +11
nop +199
acc -19
jmp -159
acc +1
jmp +253
acc +7
jmp +233
nop -76
acc +31
acc +44
jmp -18
acc +47
nop +227
jmp +178
nop -22
jmp -44
jmp +24
nop +122
acc +20
acc +43
jmp -81
acc -15
acc +10
acc +40
jmp +108
acc +45
jmp +35
acc +44
jmp +36
nop -2
nop -320
jmp +1
acc +47
jmp -6
acc -16
acc +49
nop +56
jmp +104
acc +40
jmp -159
acc +30
jmp +56
acc +47
acc -6
acc +47
acc +2
jmp -102
acc +45
jmp -262
acc +36
acc +42
acc -17
jmp -90
acc +18
nop +7
acc -14
jmp -194
acc +16
acc +31
acc +26
jmp -257
acc +25
jmp -367
jmp +69
nop -102
acc +47
jmp -356
nop -105
acc +6
jmp -42
acc +40
jmp -368
acc +42
jmp +84
acc +17
acc +14
acc -17
acc -14
jmp -80
acc +42
acc +11
acc -14
jmp -77
acc -12
acc +8
acc -19
jmp -206
acc +6
acc +18
nop +94
acc -2
jmp -330
acc -15
jmp -367
acc -15
acc +40
jmp +143
jmp -178
acc -1
jmp +140
acc +13
acc +47
jmp -271
acc +29
nop -30
nop -344
jmp -251
jmp +98
acc +45
acc -17
acc +5
jmp +1
jmp -299
acc +34
acc +7
acc +7
nop +16
jmp -106
jmp -399
jmp -291
acc -4
acc +26
jmp -376
nop -444
nop +59
acc +27
nop +89
jmp -188
acc +21
nop -246
acc +6
jmp -24
acc +35
jmp +1
jmp -361
acc +48
acc -5
acc +19
jmp +74
jmp -56
jmp +43
acc +50
nop -275
acc +39
acc -11
jmp -258
acc +8
jmp -190
acc +46
jmp +1
nop -188
acc -15
jmp +12
nop -5
nop -444
acc +0
jmp -129
acc -11
acc +28
jmp -452
acc -4
acc +24
nop -176
jmp -56
acc +47
acc +33
jmp -432
jmp -19
acc +32
jmp +1
acc +7
nop -179
jmp -49
nop -66
acc +20
jmp -122
acc +1
acc +10
acc +16
jmp +40
acc +11
acc +6
jmp -454
acc -2
acc +12
nop -228
jmp -165
acc +42
nop -212
acc +49
jmp -286
acc +42
acc +24
acc +38
jmp -440
acc +29
acc +8
acc +21
jmp -288
acc +2
jmp -427
acc +17
acc +45
acc +33
jmp -333
acc +6
jmp -445
nop -283
acc -18
jmp +1
jmp +1
jmp -492
jmp +53
acc +26
jmp -107
nop -377
jmp -155
acc +22
jmp -523
jmp -127
acc +2
nop -168
acc +15
jmp -343
acc +34
acc +0
acc +0
jmp -241
acc +30
acc +40
acc +46
acc -11
jmp -216
acc +31
jmp -86
acc +34
acc -15
nop -4
jmp -74
acc -1
acc +13
acc -2
jmp -119
acc +21
nop -516
acc +24
jmp -580
nop -200
acc +18
jmp -318
acc +0
nop -483
acc +15
acc -9
jmp -30
jmp -462
jmp -476
acc +18
acc -14
jmp -91
acc -6
acc +32
nop -611
acc +8
jmp -613
acc +23
acc +7
acc +30
acc +48
jmp -222
jmp -326
acc +46
nop -108
acc +17
acc -16
jmp +1"""

inputFile = inputFile.split("\n")
for i in range(len(inputFile)):
    inputFile[i] = inputFile[i].split(" ")
    inputFile[i][1] = int(inputFile[i][1])


print(inputFile[622:626])


def runLoop(file, verbose = False):
    line = 0
    acc = 0
    visitedLines = []
    finished = False
    
    while (line not in visitedLines) and line < len(inputFile):
        if verbose:
            print(str(line) + ", acc = " + str(acc) + ", " + str(file[line]))
        visitedLines.append(line)
        if file[line][0] == "acc":
            acc += file[line][1]
            line += 1
        elif file[line][0] == "jmp":
            line += file[line][1]
        else:
            line += 1
    if line > len(inputFile):
        finished = True
    if verbose:
        print(str(len(file)) + " " + str(line))
    print("prog finished = " + str(finished) + ", acc = " + str(acc) + ", line = " + str(line))

#print(runLoop(inputFile))

def swap(code):
    if code == "jmp":
        return "acc"
    elif code == "acc":
        return "jmp"
    elif code == "nop":
        return "nop"
    
for i in range(len(inputFile)):
    newInput = deepcopy(inputFile)
    #print("inputBefore = " + str(newInput[:5]))
    newInput[i][0] = swap(newInput[i][0])
    #print("inputAfter = " + str(newInput[:5]))
    print("i = " + str(i), end = " ")
    runLoop(newInput)
    newInput[i][0] = swap(newInput[i][0])
    #print("test with i = " + str(i) + ", " + str(newInput[:5]))
    #print(newInput[0:10])
    #print(" i was " + str(i))

#newInput[-1][0] = swap(newInput[-1][0])

"""for i in [622,624,625]:
    newInput = inputFile[:]
    newInput[i][0] = swap(newInput[i][0])

    if (i == 624):
        newInput[622][0] = swap(newInput[622][0])
    if (i == 625):
        newInput[624][0] = swap(newInput[624][0])
            
    print(newInput[622:626])
    print(newInput[-5:])

    print("#####\n" + str(i) + ":\n\n" + str(inputFile) + "^^^^^\n")
    runLoop(newInput)"""
