#f = open("building.txt",'r')
f2 = open("buildingtiqu4.txt",'r')
f3 = open("buildinginfo.txt",'w+')
true = 'true'
i=0
objlist = []
for line in open('buildingtiqu4.txt'):

    line = f2.readline()
    aa = eval(line)
    for a in aa['features']:
        if a['attributes']['objectid'] in objlist:
            continue
        else:
            objlist.append(a['attributes']['objectid'])
            li = []
            #print (type(a))
            #print (a['attributes'])
            #print (a['geometry'])
            print (a['attributes']['objectid'])
            #下面这些行，重新写个循环简化一下
            li.append(a['attributes']['objectid'])
            li.append(a['attributes']['photoid'])
            li.append(a['attributes']['建筑名称'])
            li.append(a['attributes']['建筑地址'])
            li.append(a['attributes']['地上层数'])
            li.append(a['attributes']['地下层数'])
            li.append(a['attributes']['基底面积'])
            li.append(a['attributes']['建筑面积'])
            li.append(a['attributes']['建筑结构'])
            li.append(a['attributes']['建筑用途'])
            li.append(a['attributes']['分层_jr'])
            li.append(a['attributes']['建面_jr'])
            li.append(a['attributes']['分层_ja'])
            li.append(a['attributes']['建面_ja'])
            li.append(a['attributes']['分层_jb'])
            li.append(a['attributes']['建面_jb'])
            li.append(a['attributes']['分层_jm'])
            li.append(a['attributes']['建面_jm'])
            li.append(a['attributes']['分层_jw'])
            li.append(a['attributes']['建面_jw'])
            li.append(a['attributes']['分层_js'])
            li.append(a['attributes']['建面_js'])
            li.append(a['attributes']['分层_ju'])
            li.append(a['attributes']['建面_ju'])
            li.append(a['attributes']['分层_ff'])
            li.append(a['attributes']['建面_ff'])
            li.append(a['attributes']['备注'])
            li.append(a['attributes']['行政区'])
            li.append(a['attributes']['环线范围'])
            li.append(a['attributes']['shape_Length'])
            li.append(a['attributes']['shape_Area'])
            li.append(a['geometry']['rings'])
            print(li)
            f3.writelines(str(li)+'\n')
    #i+=1
    #if i>20:
    #    break

#f.close()
f2.close()
f3.close()