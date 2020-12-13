minT = 1000066

data = """13,x,x,41,x,x,x,37,x,x,x,x,x,659,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,29,x,409,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17"""

data = data.replace("x,","").split(",")

for i in range(len(data)):
    data[i] = int(data[i])

times = []
for bus in data:
    print(str(bus))
    for j in range(0,minT+bus,bus):
        #print(str(i) + " " + str(j) + " " + str(data[i]))
        times.append([j,bus])
times = sorted(times)

f = open("times","w")
f.write(str(times))
