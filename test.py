#f = open("building.txt",'r')
f2 = open("buildingtiqu4.txt",'r')
true = 'true'
i=0
for line in open('buildingtiqu4.txt'):
    line = f2.readline()
    aa = eval(line)
    for a in aa['features']:
        print (a)
    i+=1
    if i>20:
        break

#f.close()
f2.close()