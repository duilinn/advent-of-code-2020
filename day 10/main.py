data1 = """54
91
137
156
31
70
143
51
50
18
1
149
129
151
95
148
41
144
7
125
155
14
114
108
57
118
147
24
25
73
26
8
115
44
12
47
106
120
132
121
35
105
60
9
6
65
111
133
38
138
101
126
39
78
92
53
119
136
154
140
52
15
90
30
40
64
67
139
76
32
98
113
80
13
104
86
27
61
157
79
122
59
150
89
158
107
77
112
5
83
58
21
2
66"""

data1 = data1.split("\n")

for i in range(len(data1)):
    data1[i] = int(data1[i])
data1 = sorted(data1)

def works(data):
    joltage = 0
    diff1 = 1
    diff3 = 1
    used = []

    for i in range(len(data)-1):
        adaptor = data[i]

        j = i + 1
        print("BEFORE: adaptor = " + str(adaptor) + ", i = " + str(i) + ", j = " + str(j))
                
        if (data[j] == adaptor + 1):
            diff1 += 1
        elif (data[j] == adaptor + 3):
            diff3 += 1
        elif (data[j] != adaptor + 2):
            return False
        used.append(data[j])
        
        print("AFTER: adaptor = " + str(adaptor) + ", i = " + str(i) + ", j = " + str(j))
        print("diff1 =" + str(diff1) + ", diff2 = " + str(diff3))
    return True

#print(diff1*diff3)
#print(str(len(used)) + " " + str(len(data)))
posesToDel = []
for i in range(1,len(data1)):
    if (data1[i+1] - data1[i-1]) < 4:
        posesToDel.append(i)
for i in range(len(posesToDel)):
    print(i)
"""[1, 2, 5, 6, 7, 8, 9, 12, 13, 14, 15, 18, 21, 24, 25, 26, 27, 30, 31, 32, 35, 38, 39, 40, 41, 44, 47, 50, 51, 52, 53, 54, \
57, 58, 59, 60, 61, 64, 65, 66, 67, 70, 73, 76, 77, 78, 79, 80, 83, 86, 89, 90, 91, 92, 95, 98, 101, 104, 105, 106, 107, 108, \
111, 112, 113, 114, 115, 118, 119, 120, 121, 122, 125, 126, 129, 132, 133, 136, 137, 138, 139, 140, 143, 144, 147, 148, 149, 150, \
151, 154, 155, 156, 157, 158]"""
